import os
import requests
import http.client
import json

import datetime

from .standalone import Standalone

from shufflepy.communication import Communication
from shufflepy.siem import SIEM
from shufflepy.eradication import Eradication
from shufflepy.cases import Cases
from shufflepy.assets import Assets  
from shufflepy.intel import Intel
from shufflepy.iam import IAM
from shufflepy.network import Network
from shufflepy.other import Other

http.client._MAXLINE = 524288

class Singul():

    # High default timeout due to autocorrect possibly taking time
    def __init__(self, auth="", url="https://shuffler.io", execution_id="", verify=True, timeout=300, error_on_bad_status=False, standalone=False, api_key="", apikey=""):
        if len(api_key) > 0 and not auth:
            auth = api_key

        if len(apikey) > 0 and not auth:
            auth = apikey

        if not standalone:
            if not url:
                raise ValueError("url is required")

            if len(execution_id) == 0 and os.getenv("EXECUTIONID"):
                if os.getenv("DEBUG") == "true":
                    print("Using execution_id '%s' and exec auth '%s'" % (os.getenv("EXECUTIONID"), os.getenv("AUTHORIZATION")))

                execution_id = os.getenv("EXECUTIONID")

                if not auth:
                    auth = os.getenv("AUTHORIZATION")

            if not auth:
                authkey = os.getenv('SHUFFLE_AUTHORIZATION')
                if not authkey:
                    raise ValueError("Required: SHUFFLE_AUTHORIZATION environment key OR auth=apikey")

                auth = authkey

        self.config = {
            "url": url,
            "auth": auth,
            "execution_id": execution_id,
        }
        
        self.error_on_bad_status = error_on_bad_status

        self.standalone = standalone
        self.org_id = ""
        self.verify = verify
        self.timeout = timeout
        
        # Create instances of each category
        self.communication = Communication(self)
        self.siem = SIEM(self)
        self.eradication = Eradication(self)
        self.cases = Cases(self)
        self.assets = Assets(self)
        self.intel = Intel(self)
        self.iam = IAM(self)
        self.network = Network(self)
        self.other = Other(self)

    def get_headers(self):
        auth = self.config["auth"]
        if not auth.startswith("Bearer "):
            auth = f"Bearer {auth}"

        parsedheaders = {
            "Authorization": auth,
            "User-Agent": "Singul 0.0.1",
        }

        # Overrides the current org
        if self.org_id:
            parsedheaders["Org-Id"] = self.org_id

        return parsedheaders

    def remove_binary(self):
        standalone = Standalone()
        path = standalone.get_executable_path()

        if os.path.isfile(path):
            os.remove(path)
        else:
            print("File not found: %s" % path)

    def run_workflow(self, workflow_id="", start_command="", wait=True, runtime_argument="", execution_argument="", startnode="", org_id="", auth="", auth_id="", authentication_id=""):
        # Check if UUID length
        if len(workflow_id) != 36:
            raise ValueError("workflow_id must be 36 in length (UUID)")

        if auth and not auth_id:
            auth_id = auth

        if authentication_id and not auth_id:
            auth_id = authentication_id

        if not start_command:
            if runtime_argument:
                start_command = runtime_argument
            elif execution_argument:
                start_command = execution_argument

        parsedurl = "%s/api/v1/workflows/%s/run" % (self.config["url"], workflow_id)
        requestdata = {
            "execution_argument": start_command,
            "start": startnode,
        }

        if self.config["execution_id"]:
            #parsedurl += f"?execution_id={self.config['execution_id']}&authorization={self.config['auth']}"
            parsedurl += f"?execution_id={self.config['execution_id']}&source_auth={self.config['auth']}"
            #requestdata["source_execution"] = self.config["execution_id"]
            #requestdata["source_auth"] = self.config["auth"]

        if str(wait).lower() == "true":
            if "?" in parsedurl:
                parsedurl += "&wait=true"
            else:
                parsedurl += "?wait=true"

        parsedheaders = self.get_headers()
        if org_id:
            parsedheaders["Org-Id"] = org_id

        response = requests.post(
            parsedurl, 
            json=requestdata, 
            headers=parsedheaders,
            verify=self.verify,
            timeout=self.timeout,
        )

        if (response.status_code != 200) and self.error_on_bad_status:
            raise ValueError(f"Status Error ({response.status_code}): {response.text}")

        try:
            respdata = response.json()
            return respdata
        except Exception as e:
            raise ValueError(f"Json Error ({response.status_code}): {response.text}")

    def run_app(self, app_id="", action="", auth_id="", parameters={}, org_id="", auth="", authentication_id="", params={}):
        if len(app_id) != 32:
            raise ValueError("app_id is required and must be 32 in length (md5)")

        if len(action) == 0:
            raise ValueError("action is required")

        if auth and not auth_id:
            auth_id = auth
        elif authentication_id and not auth_id:
            auth_id = authentication_id

        if params and not parameters:
            parameters = params

        parsedurl = "%s/api/v1/apps/%s/run" % (self.config["url"], app_id)
        parsedheaders = self.get_headers()

        print("Using URL: %s" % parsedurl)

        if org_id:
            parsedheaders["Org-Id"] = org_id

        if not isinstance(parameters, dict) and not isinstance(parameters, list):
            raise ValueError("Parameters must be a dictionary of key:values or list of [{name: name, value:value}]")

        if self.config["execution_id"]:
            parsedurl += f"?execution_id={self.config['execution_id']}&authorization={self.config['auth']}"

        # Check if parameters is a dict. If it is is, map key: value to parameters
        params = []
        if isinstance(parameters, list):
            params = parameters
        elif parameters:
            for key, value in parameters.items():
                params.append({
                    "name": key,
                    "value": value,
                })
        else:
            print("Running with no parameters")

        requestdata = {
            "app_id": app_id,
            "name": action,
            "authentication_id": auth_id,
            "parameters": params,
        }

        response = requests.post(
            parsedurl, 
            json=requestdata, 
            headers=parsedheaders,
            verify=self.verify,
            timeout=self.timeout,
        )

        if response.status_code != 200 and self.error_on_bad_status:
            raise ValueError(f"Status Error ({response.status_code}): {response.text}")

        try:
            respdata = response.json()
            try:
                return json.loads(respdata["result"])
            except Exception as e:
                return respdata
        except Exception as e:
            raise ValueError(f"Json Error ({response.status_code}): {response.text}")

    def run(self, app="", action="", org_id="", category="", skip_workflow=True, auth_id="", authentication_id="", fields=[], params={}, **kwargs):
        return connect(app=app, action=action, org_id=org_id, category=category, skip_workflow=skip_workflow, auth_id=auth_id, authentication_id=authentication_id, fields=fields, params=params, **kwargs)

    def run_agent(self, ai_action, environment="", appname="", allowe_actions=""):
        if self.standalone:
            standalone = Standalone()
            return standalone.run_agent()

        if len(ai_action) < 5:
            raise ValueError("user_action is required and must be at least 5 characters in length")

        if environment == "":
            environment = "cloud"
        if appname == "":
            appname = "openai"
        if allowed_actions == "":
            allowed_actions = "API"

        # This API's URL is silly 
        parsedurl = self.config["url"]
        if not "/api/v1/" in parsedurl:
            parsedurl += "/api/v1/apps/agent/run"

        parsedheaders = self.get_headers()
        if org_id: 
            parsedheaders["Org-Id"] = org_id

        self.config["category"] = category
        requestdata = {
            "app_id": "shuffle_agent",
            "app_name": "AI Agent",
            "app_version": "1.0.0",
            "environment": environment,
            "name": "agent",
            "parameters": [{
                "name": "appname",
                "value": appname,
            },
            {
                "name": "input",
                "value": ai_action,
            },
            {
                "name": "action",
                "value": allowed_actions,
            }]
        }

        response = requests.post(
            parsedurl, 
            json=requestdata, 
            headers=parsedheaders,
            verify=self.verify,
            timeout=self.timeout,
        )

        if response.status_code != 200 and self.error_on_bad_status:
            raise ValueError(f"Status Error ({response.status_code}): {response.text}")

        try:
            respdata = response.json()
        except:
            raise ValueError(f"Json Error ({response.status_code}): {response.text}")

        return respdata


    def connect(self, app="", action="", org_id="", category="", skip_workflow=True, auth_id="", authentication_id="", fields=[], params={}, environment="", skip_authentication=False, **kwargs):
        if self.standalone:
            standalone = Standalone()
            return standalone.connect(app=app, action=action, org_id=org_id, category=category, skip_workflow=skip_workflow, auth_id=auth_id, authentication_id=authentication_id, fields=fields, params=params, **kwargs)

        if not category and not app:
            raise ValueError("category or app is required. Example: app=\"jira\"")

        if not action:
            raise ValueError("action is required. Example: action=\"list_tickets\"")

        # This API's URL is silly 
        parsedurl = self.config["url"]
        if not "/api/v1/" in parsedurl:
            parsedurl += "/api/v1/apps/categories/run"

        parsedheaders = self.get_headers()
        if org_id: 
            parsedheaders["Org-Id"] = org_id

        self.config["category"] = category
        requestdata = {
            "skip_workflow": True,
            "action": action,
        }

        if params and not fields:
            fields = params

        for key in kwargs:
            if key not in fields:
                fields[key] = kwargs[key]

        if fields:
            requestdata["fields"] = fields
            
        if environment:
            requestdata["environment"] = environment

        if app:
            requestdata["app"] = app

        if category:
            requestdata["category"] = category

        if skip_workflow == False:
            requestdata["skip_workflow"] = False

        if auth_id:
            requestdata["authentication_id"] = auth_id

        if authentication_id:
            requestdata["authentication_id"] = authentication_id
        
        if skip_authentication:
            requestdata["skip_authentication"] = skip_authentication

        if self.config["execution_id"]:
            if "?" in parsedurl:
                parsedurl += f"&execution_id={self.config['execution_id']}&authorization={self.config['auth']}"
            else:
                parsedurl += f"?execution_id={self.config['execution_id']}&authorization={self.config['auth']}"
            
            
        response = requests.post(
            parsedurl, 
            json=requestdata, 
            headers=parsedheaders,
            verify=self.verify,
            timeout=self.timeout,
        )

        if response.status_code != 200 and self.error_on_bad_status:
            raise ValueError(f"Status Error ({response.status_code}): {response.text}")

        try:
            respdata = response.json()
        except:
            raise ValueError(f"Json Error ({response.status_code}): {response.text}")

        return respdata
