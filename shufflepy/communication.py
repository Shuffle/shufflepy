from .base import BaseCategory

class Communication(BaseCategory):
    def __init__(self, singul):
        super().__init__(singul)
        self.category = "communication"
        
    def list_messages(self, app="", org_id="", fields=[], auth_id=""):
        return self._connect(
            action="list_messages",
            app=app,
            org_id=org_id,
            fields=fields,
            auth_id=auth_id
        )

    def send_message(self, app="", org_id="", fields=[], auth_id=""):
        return self._connect(
            action="send_message",
            app=app,
            org_id=org_id,
            fields=fields,
            auth_id=auth_id
        )

    def get_message(self, app="", org_id="", fields=[], auth_id=""):
        return self._connect(
            action="get_message",
            app=app,
            org_id=org_id,
            fields=fields,
            auth_id=auth_id
        )

    def search_messages(self, app="", org_id="", fields=[], auth_id=""):
        return self._connect(
            action="search_messages",
            app=app,
            org_id=org_id,
            fields=fields,
            auth_id=auth_id
        )

    def list_attachments(self, app="", org_id="", fields=[], auth_id=""):
        return self._connect(
            action="list_attachments",
            app=app,
            org_id=org_id,
            fields=fields,
            auth_id=auth_id
        )

    def get_attachment(self, app="", org_id="", fields=[], auth_id=""):
        return self._connect(
            action="get_attachment",
            app=app,
            org_id=org_id,
            fields=fields,
            auth_id=auth_id
        )
        
    def create_contact(self, app="", org_id="", fields=[], auth_id=""):
        return self._connect(
            action="create_contact",
            app=app,
            org_id=org_id,
            fields=fields,
            auth_id=auth_id
        )

    def get_contact(self, app="", org_id="", fields=[], auth_id=""):
        return self._connect(
            action="get_contact",
            app=app,
            org_id=org_id,
            fields=fields,
            auth_id=auth_id
        )