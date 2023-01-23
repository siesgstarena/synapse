import os
import flask_admin as admin
from flask_session import Session
from models.problem import ProblemModel, ProblemView
from routes import index, training, recommend, auth_route
from db.mongo import init_mongo
from storage.firebase import init_firebase
from middleware.auth import AdminIndexView
from middleware.access_token import VerifyAccessToken
from .extensions import mail


def create_app(app, config_file="settings.py"):
    dirname = os.path.dirname(__file__)
    config_file = os.path.join(dirname, config_file)
    app.config.from_pyfile(config_file)
    init_firebase()
    mail.init_app(app)
    app = init_mongo(app)
    Session(app)
    app.wsgi_app = VerifyAccessToken(app.wsgi_app)
    app.register_blueprint(index, url_prefix="/")
    app.register_blueprint(auth_route, url_prefix="/auth")
    app.register_blueprint(training, url_prefix="/problem/training")
    app.register_blueprint(recommend, url_prefix="/problem/recommend")
    admins = admin.Admin(
        app,
        "Arena: Recommendation System",
        template_mode="bootstrap4",
        index_view=AdminIndexView(),
    )
    admins.add_view(ProblemView(ProblemModel))
    return app
