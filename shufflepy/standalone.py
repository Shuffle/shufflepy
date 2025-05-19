import os
import sys
import json
import time
import requests

import pty
import select
import subprocess
from tqdm import tqdm

class Standalone():
    def __init__(self):
        self.debug = os.getenv("DEBUG", "false")
        pass

    def download_executable(self, executable):
        if len(executable) == 0:
            executable = self.get_executable_path()

        # 6 different urls (2 for each OS)
        downloadVersion = "v0.0.8"
        cur_os = "linux"  # or "windows" or "macos"
        downloadType = "amd64"
        if os.uname()[0] == "Darwin":
            cur_os = "darwin"
            if os.uname()[4].startswith("arm64"):
                downloadType = "arm64"
        elif os.name == "nt":
            cur_os = "windows"
            if os.uname()[4].startswith("arm64"):
                downloadType = "arm64"
        elif os.name == "posix":
            cur_os = "linux"
            if os.uname()[4].startswith("arm64"):
                downloadType = "arm64"
        else:
            raise ValueError("Couldn't find OS %s with arch %s" % (os.uname()[0], os.uname()[4]))

        url = "https://github.com/Shuffle/Singul/releases/download/%s/singul-%s-%s" % (downloadVersion, cur_os, downloadType)
        if os.name == "nt":
            url += ".exe"

        # Download the file into the executable path
        print("Downloading %s to %s to run Singul locally." % (url, executable))
        if os.name == "nt":
            os.makedirs(os.path.dirname(executable), exist_ok=True)
        else:
            os.makedirs(os.path.dirname(executable), exist_ok=True)

        with requests.get(url, stream=True) as r:
            r.raise_for_status()
            total_size = int(r.headers.get('content-length', 0))
            block_size = 1024  # 1 Kibibyte
            with open(executable, 'wb') as f, tqdm(
                total=total_size, unit='iB', unit_scale=True
            ) as bar:
                for chunk in r.iter_content(chunk_size=block_size):
                    f.write(chunk)
                    bar.update(len(chunk))

    def run_interactive_windows(self, executable, args=[], timeout=90):
        import pywinpty

        output = []

        # Create a pseudo-terminal
        winpty = pywinpty.PTY(spawn=False)
        proc = subprocess.Popen(
            command,
            stdin=winpty.spawn_process(),
            stdout=winpty.spawn_process(),
            stderr=winpty.spawn_process(),
            bufsize=0
        )

        def reader():
            while True:
                try:
                    data = winpty.read(1024)
                    if not data:
                        break
                    sys.stdout.write(data.decode(errors="ignore"))
                    sys.stdout.flush()
                    output.append(data.decode(errors="ignore"))
                except Exception:
                    break

        def writer():
            try:
                while True:
                    user_input = sys.stdin.read(1)
                    if user_input:
                        winpty.write(user_input.encode())
            except Exception:
                pass

        reader_thread = threading.Thread(target=reader)
        writer_thread = threading.Thread(target=writer)
        reader_thread.daemon = True
        writer_thread.daemon = True
        reader_thread.start()
        writer_thread.start()

        start = time.time()
        while time.time() - start < timeout and proc.poll() is None:
            time.sleep(0.1)

        if proc.poll() is None:
            print("\n[!] Timeout reached (windows). Terminating process.", file=sys.stderr)
            proc.terminate()

        proc.wait()
        return ''.join(output)

    def run_interactive(self, executable, args=[], timeout=90):
        if self.debug == "true":
            print("===== Singul exec: %s with args %s (python) =====" % (executable, " ".join(args)))

        if os.name == "nt":
            return run_interactive_windows(executable, args=args, timeout=timeout)

        # Spawn a pseudo-terminal so input/output works interactively
        master_fd, slave_fd = pty.openpty()

        proc = subprocess.Popen(
            [executable] + args,
            stdin=slave_fd,
            stdout=slave_fd,
            stderr=slave_fd,
            close_fds=True,
            #text=True,
        )

        os.close(slave_fd)

        output = ""
        start_time = time.time()

        try:
            while True:
                if time.time() - start_time > timeout:
                    print("\n[!] Timeout reached after %d seconds. Killing subprocess.\n" % timeout, file=sys.stderr)
                    proc.terminate()
                    break

                rlist, _, _ = select.select([master_fd, sys.stdin], [], [], 0.1)
                # User typed something: send to process
                if sys.stdin in rlist:
                    user_input = os.read(sys.stdin.fileno(), 1024)
                    os.write(master_fd, user_input)

                if master_fd in rlist:
                    try:
                        data = os.read(master_fd, 1024)
                        if not data:
                            break

                        sys.stdout.buffer.write(data)
                        sys.stdout.flush()
                        output += data.decode(errors='ignore')
                    except OSError:
                        break

                if proc.poll() is not None:
                    break

        except KeyboardInterrupt:
            proc.terminate()

        finally:
            os.close(master_fd)
            proc.wait()
            #os.close(slave_fd)

        if self.debug == "true":
            print("===== Singul exec: %s with args %s (python) =====" % (executable, " ".join(args)))

        return output

    def run_singul(self, executable, app="", action="", org_id="", category="", skip_workflow=True, auth_id="", authentication_id="", fields=[], params={}, **kwargs):
        if not os.getenv("OPENAI_API_KEY"): 
            raise ValueError("\n\nOPENAI_API_KEY must be set to your OpenAI API key for translations to work the first time. See https://github.com/Shuffle/singul#llm-controls for using other LLMs\n")

        if params and not fields:
            print("WARNING: Parameters passed without fields. This may not work as expected.")
            fields = params

        newfields = {}
        if isinstance(fields, dict):
            newfields = fields
        elif isinstance(fields, list):
            for field in fields:
                if isinstance(field, str):
                    newfields[field] = ""
                    continue

                keyname = "name"
                if keyname not in field:
                    keyname = "key"

                if isinstance(field, dict):
                    newfields[field[keyname]] = field["value"]
                else:
                    raise ValueError("Field must be a dict with name and value keys")
        else:
            print("Fields must be a dict or list of dicts")

        # Loop through kwargs and add them
        for key in kwargs:
            if key not in newfields:
                newfields[key] = kwargs[key]


        all_args = [action, app]
        command = "%s %s %s" % (executable, action, app)
        for key, value in newfields.items():
            command += " --%s='%s'" % (key, value)
            all_args.append("--%s='%s'" % (key, value))

        timeout = 90 
        if os.getenv("SINGUL_TIMEOUT"):
            timeout = int(os.getenv("SINGUL_TIMEOUT"))

        #stdout = self.run_interactive(executable, args=all_args, timeout=90)
        captured_output = self.run_interactive(executable, args=all_args, timeout=timeout)
        record = False
        all_lines = []
        for line in captured_output.splitlines():
            if record and line:
                all_lines.append(line)

            if "= API OUTPUT =" in line:
                record = True

        if all_lines:
            captured_output = "\n".join(all_lines)

        try:
            captured_output = json.loads(captured_output)
        except Exception as e:
            return {
                "value": captured_output,
            }

        return captured_output

    def get_executable_path(self):
        if len(os.getenv("SINGUL_EXECUTABLE", "")) > 0:
            return os.path.expanduser(os.getenv("SINGUL_EXECUTABLE"))

        # Check if macos arm
        executable = ""
        if os.uname()[0] == "Darwin" and os.uname()[4].startswith("arm64"):
            executable = "~/Library/Caches/singul/singul"
        elif os.name == "nt":
            executable = "%LOCALAPPDATA%\\singul\\singul.exe"
        elif os.name == "posix": 
            executable = "~/.cache/singul/singul"

        else:
            raise ValueError("Unsupported OS: %s. Please contact support@shuffler.io" % os.uname()[0])

        path = os.path.expanduser(executable)
        return path

    # We are passing along ALL arguments in case these will be useful in the future
    # E.g. if local singul should use remote auth from singul cloud
    # Or if we want to run singul remotely from singul.go -> singul cloud etc.
    def connect(self, app="", action="", org_id="", category="", skip_workflow=True, auth_id="", authentication_id="", fields=[], params={}, **kwargs):
        path = self.get_executable_path()
        if not os.path.isfile(path):
            self.download_executable(path)

        # Check if the path is executable or not
        if not os.access(path, os.X_OK):
            # Change it
            os.chmod(path, 0o755)

        if not os.access(path, os.X_OK):
            raise ValueError("Singul executable is not executable: %s. Please run chmod +x or similar to make it possible to run it." % path)

        return self.run_singul(path, app=app, action=action, org_id=org_id, category=category, skip_workflow=skip_workflow, auth_id=auth_id, authentication_id=authentication_id, fields=fields, params=params, **kwargs)
