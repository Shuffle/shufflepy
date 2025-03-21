from .base import BaseCategory

class Other(BaseCategory):
    def __init__(self, singul):
        super().__init__(singul)
        self.category = "other"
        
    def update_info(self, app="", org_id="", fields=[], auth_id=""):
        return self._connect(
            action="update_info",
            app=app,
            org_id=org_id,
            fields=fields,
            auth_id=auth_id
        )

    def get_info(self, app="", org_id="", fields=[], auth_id=""):
        return self._connect(
            action="get_info",
            app=app,
            org_id=org_id,
            fields=fields,
            auth_id=auth_id
        )

    def get_status(self, app="", org_id="", fields=[], auth_id=""):
        return self._connect(
            action="get_status",
            app=app,
            org_id=org_id,
            fields=fields,
            auth_id=auth_id
        )

    def get_version(self, app="", org_id="", fields=[], auth_id=""):
        return self._connect(
            action="get_version",
            app=app,
            org_id=org_id,
            fields=fields,
            auth_id=auth_id
        )

    def get_health(self, app="", org_id="", fields=[], auth_id=""):
        return self._connect(
            action="get_health",
            app=app,
            org_id=org_id,
            fields=fields,
            auth_id=auth_id
        )

    def get_config(self, app="", org_id="", fields=[], auth_id=""):
        return self._connect(
            action="get_config",
            app=app,
            org_id=org_id,
            fields=fields,
            auth_id=auth_id
        )

    def get_configs(self, app="", org_id="", fields=[], auth_id=""):
        return self._connect(
            action="get_configs",
            app=app,
            org_id=org_id,
            fields=fields,
            auth_id=auth_id
        )

    def get_configs_by_type(self, app="", org_id="", fields=[], auth_id=""):
        return self._connect(
            action="get_configs_by_type",
            app=app,
            org_id=org_id,
            fields=fields,
            auth_id=auth_id
        )

    def get_configs_by_name(self, app="", org_id="", fields=[], auth_id=""):
        return self._connect(
            action="get_configs_by_name",
            app=app,
            org_id=org_id,
            fields=fields,
            auth_id=auth_id
        )

    def run_script(self, app="", org_id="", fields=[], auth_id=""):
        return self._connect(
            action="run_script",
            app=app,
            org_id=org_id,
            fields=fields,
            auth_id=auth_id,
        )