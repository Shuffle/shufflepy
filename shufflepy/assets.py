from .base import BaseCategory

class Assets(BaseCategory):
    def __init__(self, singul):
        super().__init__(singul)
        self.category = "assets"
        
    def list_assets(self, app="", org_id="", fields=[], auth_id=""):
        return self._connect(
            action="list_assets",
            app=app,
            org_id=org_id,
            fields=fields,
            auth_id=auth_id
        )

    def get_asset(self, app="", org_id="", fields=[], auth_id=""):
        return self._connect(
            action="get_asset",
            app=app,
            org_id=org_id,
            fields=fields,
            auth_id=auth_id
        )

    def search_assets(self, app="", org_id="", fields=[], auth_id=""):
        return self._connect(
            action="search_assets",
            app=app,
            org_id=org_id,
            fields=fields,
            auth_id=auth_id
        )

    def search_users(self, app="", org_id="", fields=[], auth_id=""):
        return self._connect(
            action="search_users",
            app=app,
            org_id=org_id,
            fields=fields,
            auth_id=auth_id
        )

    def search_endpoints(self, app="", org_id="", fields=[], auth_id=""):
        return self._connect(
            action="search_endpoints",
            app=app,
            org_id=org_id,
            fields=fields,
            auth_id=auth_id
        )

    def search_vulnerabilities(self, app="", org_id="", fields=[], auth_id=""):
        return self._connect(
            action="search_vulnerabilities",
            app=app,
            org_id=org_id,
            fields=fields,
            auth_id=auth_id
        )