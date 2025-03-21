from .base import BaseCategory

class Intel(BaseCategory):
    def __init__(self, singul):
        super().__init__(singul)
        self.category = "intel"
        
    def get_ioc(self, app="", org_id="", fields=[], auth_id=""):
        return self._connect(
            action="get_ioc",
            app=app,
            org_id=org_id,
            fields=fields,
            auth_id=auth_id
        )

    def search_ioc(self, app="", org_id="", fields=[], auth_id=""):
        return self._connect(
            action="search_ioc",
            app=app,
            org_id=org_id,
            fields=fields,
            auth_id=auth_id
        )

    def create_ioc(self, app="", org_id="", fields=[], auth_id=""):
        return self._connect(
            action="create_ioc",
            app=app,
            org_id=org_id,
            fields=fields,
            auth_id=auth_id
        )

    def update_ioc(self, app="", org_id="", fields=[], auth_id=""):
        return self._connect(
            action="update_ioc",
            app=app,
            org_id=org_id,
            fields=fields,
            auth_id=auth_id
        )

    def delete_ioc(self, app="", org_id="", fields=[], auth_id=""):
        return self._connect(
            action="delete_ioc",
            app=app,
            org_id=org_id,
            fields=fields,
            auth_id=auth_id
        )