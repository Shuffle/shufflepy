from .base import BaseCategory

class Network(BaseCategory):
    def __init__(self, singul):
        super().__init__(singul)
        self.category = "network"
        
    def get_rules(self, app="", org_id="", fields=[], auth_id=""):
        return self._connect(
            action="get_rules",
            app=app,
            org_id=org_id,
            fields=fields,
            auth_id=auth_id
        )

    def allow_ip(self, app="", org_id="", fields=[], auth_id=""):
        return self._connect(
            action="allow_ip",
            app=app,
            org_id=org_id,
            fields=fields,
            auth_id=auth_id
        )

    def block_ip(self, app="", org_id="", fields=[], auth_id=""):
        return self._connect(
            action="block_ip",
            app=app,
            org_id=org_id,
            fields=fields,
            auth_id=auth_id
        )