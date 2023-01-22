import flask_admin as admin
from flask import session


class AdminIndexView(admin.AdminIndexView):
    def is_accessible(self):
        return session.get("admin", False)
