from .base import BaseCategory

class Cases(BaseCategory):
    def __init__(self, singul):
        super().__init__(singul)
        self.category = "cases"
        
    def list_tickets(self, app="", org_id="", fields=[], auth_id=""):
        return self._connect(
            action="list_tickets",
            app=app,
            org_id=org_id,
            fields=fields,
            auth_id=auth_id
        )

    def get_ticket(self, app="", org_id="", fields=[], auth_id=""):
        return self._connect(
            action="get_ticket",
            app=app,
            org_id=org_id,
            fields=fields,
            auth_id=auth_id
        )

    def create_ticket(self, app="", org_id="", fields=[], auth_id=""):
        return self._connect(
            action="create_ticket",
            app=app,
            org_id=org_id,
            fields=fields,
            auth_id=auth_id
        )

    def close_ticket(self, app="", org_id="", fields=[], auth_id=""):
        return self._connect(
            action="close_ticket",
            app=app,
            org_id=org_id,
            fields=fields,
            auth_id=auth_id
        )

    def add_comment(self, app="", org_id="", fields=[], auth_id=""):
        return self._connect(
            action="add_comment",
            app=app,
            org_id=org_id,
            fields=fields,
            auth_id=auth_id
        )

    def update_ticket(self, app="", org_id="", fields=[], auth_id=""):
        return self._connect(
            action="update_ticket",
            app=app,
            org_id=org_id,
            fields=fields,
            auth_id=auth_id
        )

    def search_tickets(self, app="", org_id="", fields=[], auth_id=""):
        return self._connect(
            action="search_tickets",
            app=app,
            org_id=org_id,
            fields=fields,
            auth_id=auth_id
        )