class BaseCategory:
    def __init__(self, singul):
        self.singul = singul
        self.category = self.__class__.__name__.lower()
        
    def _connect(self, action, app="", org_id="", fields=[], auth_id="", skip_workflow=True):
        return self.singul.connect(
            app=app,
            action=action,
            org_id=org_id,
            fields=fields,
            auth_id=auth_id,
            category=self.category,
            skip_workflow=skip_workflow
        )