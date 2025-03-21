from .base import BaseCategory

class SIEM(BaseCategory):
    def __init__(self, singul):
        super().__init__(singul)
        self.category = "siem"
        
    def search(self, app="", org_id="", fields=[], auth_id=""):
        return self._connect(
            action="search",
            app=app,
            org_id=org_id,
            fields=fields,
            auth_id=auth_id
        )

    def list_alerts(self, app="", org_id="", fields=[], auth_id=""):
        return self._connect(
            action="list_alerts",
            app=app,
            org_id=org_id,
            fields=fields,
            auth_id=auth_id
        )

    def close_alert(self, app="", org_id="", fields=[], auth_id=""):
        return self._connect(
            action="close_alert",
            app=app,
            org_id=org_id,
            fields=fields,
            auth_id=auth_id
        )

    def get_alert(self, app="", org_id="", fields=[], auth_id=""):
        return self._connect(
            action="get_alert",
            app=app,
            org_id=org_id,
            fields=fields,
            auth_id=auth_id
        )

    def create_detection(self, app="", org_id="", fields=[], auth_id=""):
        return self._connect(
            action="create_detection",
            app=app,
            org_id=org_id,
            fields=fields,
            auth_id=auth_id
        )

    def add_to_lookup_list(self, app="", org_id="", fields=[], auth_id=""):
        return self._connect(
            action="add_to_lookup_list",
            app=app,
            org_id=org_id,
            fields=fields,
            auth_id=auth_id
        )

    def isolate_endpoint(self, app="", org_id="", fields=[], auth_id=""):
        return self._connect(
            action="isolate_endpoint",
            app=app,
            org_id=org_id,
            fields=fields,
            auth_id=auth_id
        )