import requests

class Shuffle():
    def __init__(self, config, verify=False, timeout=10):
        self.config = config
        self.verify = verify
        self.timeout = timeout

    def config(self, url="https://shuffler.io", auth=""):
        if not url:
            raise ValueError("url is required")

        if not auth:
            raise ValueError("auth is required")

        self.config = {
            "url": url,
            "auth": auth
        }

    def get_headers(self):
        auth = self.config["auth"]
        if "Bearer" not in auth:
            auth = f"Bearer {auth}"

        return {
            "Authorization": self.config["auth"],
            "User-Agent": "Shufflepy 0.0.1",
        }

    def connect(self, category="", app="", action="", fields={}):
        if not category and not app:
            raise ValueError("category or app is required. Example: app=\"ticket\"")

        if not action:
            raise ValueError("action is required. Example: action=\"list_tickets\"")


        self.config["category"] = category
        requestdata = {
            "action": action,
        }

        if fields:
            requestdata["fields"] = fields

        if app:
            requestdata["app"] = app

        if category:
            requestdata["category"] = category

        headers = self.get_headers() 
        response = requests.post(
            self.config["url"], 
            json=requestdata, 
            headers=self.get_headers(),
            verify=self.verify,
            timeout=self.timeout,
        )

        respdata = response.json()

        if response.status_code != 200:
            raise ValueError(f"Error ({response.status_code}): {respdata}")

        return respdata
