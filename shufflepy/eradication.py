from .base import BaseCategory

class Eradication(BaseCategory):
    def __init__(self, singul):
        super().__init__(singul)
        self.category = "eradication"
        
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

    def block_hash(self, app="", org_id="", fields=[], auth_id=""):
        return self._connect(
            action="block_hash",
            app=app,
            org_id=org_id,
            fields=fields,
            auth_id=auth_id
        )

    def search_hosts(self, app="", org_id="", fields=[], auth_id=""):
        return self._connect(
            action="search_hosts",
            app=app,
            org_id=org_id,
            fields=fields,
            auth_id=auth_id
        )

    def isolate_host(self, app="", org_id="", fields=[], auth_id=""):
        return self._connect(
            action="isolate_host",
            app=app,
            org_id=org_id,
            fields=fields,
            auth_id=auth_id
        )

    def unisolate_host(self, app="", org_id="", fields=[], auth_id=""):
        return self._connect(
            action="unisolate_host",
            app=app,
            org_id=org_id,
            fields=fields,
            auth_id=auth_id
        )

    def trigger_host_scan(self, app="", org_id="", fields=[], auth_id=""):
        return self._connect(
            action="trigger_host_scan",
            app=app,
            org_id=org_id,
            fields=fields,
            auth_id=auth_id
        )