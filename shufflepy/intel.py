from .base import BaseCategory

class Intel(BaseCategory):
    def __init__(self, singul):
        super().__init__(singul)
        self.category = "intel"
    
    # We only need one method to fetch IOC data, since both 'search' and 'get' perform the same operation.
        
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

    # Cannot create the IOC because it was created by the Virustotal integration
    def create_ioc(self, app="", org_id="", fields=[], auth_id=""):
        return self._connect(
            action="create_ioc",
            app=app,
            org_id=org_id,
            fields=fields,
            auth_id=auth_id
        )

    # Update method is required because we can update the IOC
    def update_ioc(self, app="", org_id="", fields=[], auth_id=""):
        return self._connect(
            action="update_ioc",
            app=app,
            org_id=org_id,
            fields=fields,
            auth_id=auth_id
        )

    # Cannot delete the IOC because it is managed by Virustotal, so delete is not allowed
    def delete_ioc(self, app="", org_id="", fields=[], auth_id=""):
        return self._connect(
            action="delete_ioc",
            app=app,
            org_id=org_id,
            fields=fields,
            auth_id=auth_id
        )