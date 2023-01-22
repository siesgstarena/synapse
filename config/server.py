import flask_admin as admin
from flask import session
from flask_session import Session
from models.problem import ProblemModel, ProblemView
from routes import index, training, recommend, admin_route
from db.mongo import init_mongo
from storage.firebase import init_firebase


class MyAdminIndexView(admin.AdminIndexView):
    def is_accessible(self):
        return session.get("admin", False)


def create_app(app):
    init_firebase()
    app = init_mongo(app)
    app.config["SESSION_PERMANENT"] = False
    app.config["SESSION_TYPE"] = "filesystem"
    Session(app)
    app.register_blueprint(index, url_prefix="/")
    app.register_blueprint(training, url_prefix="/problem/training")
    app.register_blueprint(recommend, url_prefix="/problem/recommend")
    app.register_blueprint(admin_route, url_prefix="/admin")
    admins = admin.Admin(
        app,
        "Arena: Recommendation System",
        template_mode="bootstrap4",
        index_view=MyAdminIndexView(),
    )
    admins.add_view(ProblemView(ProblemModel))
    return app
