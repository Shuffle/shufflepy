from .base import BaseCategory

class IAM(BaseCategory):
    def __init__(self, singul):
        super().__init__(singul)
        self.category = "iam"
        
    def reset_password(self, app="", org_id="", fields=[], auth_id=""):
        return self._connect(
            action="reset_password",
            app=app,
            org_id=org_id,
            fields=fields,
            auth_id=auth_id
        )

    def enable_user(self, app="", org_id="", fields=[], auth_id=""):
        return self._connect(
            action="enable_user",
            app=app,
            org_id=org_id,
            fields=fields,
            auth_id=auth_id
        )

    def disable_user(self, app="", org_id="", fields=[], auth_id=""):
        return self._connect(
            action="disable_user",
            app=app,
            org_id=org_id,
            fields=fields,
            auth_id=auth_id
        )

    def get_identity(self, app="", org_id="", fields=[], auth_id=""):
        return self._connect(
            action="get_identity",
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

    def search_identity(self, app="", org_id="", fields=[], auth_id=""):
        return self._connect(
            action="search_identity",
            app=app,
            org_id=org_id,
            fields=fields,
            auth_id=auth_id
        )