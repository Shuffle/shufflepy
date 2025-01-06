import os
import requests
import http.client
http.client._MAXLINE = 524288 

class Shuffle():

    # High default timeout due to autocorrect possibly taking time
    def __init__(self, auth="", url="https://shuffler.io", verify=True, timeout=60):
        if not url:
            raise ValueError("url is required")

        if not auth:
            authkey = os.environ.get('SHUFFLE_AUTHORIZATION')
            if not authkey:
                raise ValueError("Required: SHUFFLE_AUTHORIZATION environment key OR auth=apikey")

            auth = authkey

        self.config = {
            "url": url,
            "auth": auth
        }

        self.org_id = ""
        self.verify = verify
        self.timeout = timeout

    def get_headers(self):
        auth = self.config["auth"]
        if not auth.startswith("Bearer "):
            auth = f"Bearer {auth}"


        parsedheaders = {
            "Authorization": auth,
            "User-Agent": "Shufflepy 0.0.1",
        }

        # Overrides the current org
        if self.org_id:
            parsedheaders["Org-Id"] = self.org_id

        return parsedheaders

    def connect(self, app="", action="", org_id="", category="", skip_workflow=True, auth_id="", authentication_id="", fields={}, **kwargs):
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

        if fields:
            requestdata["fields"] = fields

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

        headers = self.get_headers() 
        response = requests.post(
            parsedurl, 
            json=requestdata, 
            headers=parsedheaders,
            verify=self.verify,
            timeout=self.timeout,
        )

        if response.status_code != 200:
            raise ValueError(f"Status Error ({response.status_code}): {response.text}")

        try:
            respdata = response.json()
        except:
            raise ValueError(f"Json Error ({response.status_code}): {response.text}")

        return respdata

    def send_message(self, app="", org_id="", fields={}):
        return self.connect(
            app=app,
            action="send_message",
            org_id=org_id,
            fields=fields,
        )

    def list_tickets(self, app="", org_id="", fields={}, auth_id=""):
        return self.connect(
            app=app,
            action="list_tickets",
            org_id=org_id,
            fields=fields,
            auth_id=auth_id,
        )

    def create_ticket(self, app="", org_id="", fields={}):
        return self.connect(
            app=app,
            action="create_ticket",
            org_id=org_id,
            fields=fields
        )

if __name__ == "__main__":
    import os
    shuffle = Shuffle(
        os.environ.get("SHUFFLE_AUTHORIZATION"),
        url="http://localhost:5002", # Used for testing
    )

    resp = shuffle.list_alerts(app="jira")
    print(resp)

    #resp = shuffle.send_message(app="whatsapp")
    #print(resp)

    #resp = shuffle.send_message(app="discord")
    #print(resp)

    #resp = shuffle.list_tickets(app="monday")
    #print(resp)

    #resp = shuffle.list_tickets(app="github")
    #print(resp)

    #resp = shuffle.create_ticket(app="jira") 
    #print(resp)

    #resp = shuffle.create_ticket(app="github") 
    #print(resp)
