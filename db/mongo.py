import os
from . import db


def init_mongo(app):
    app.config["SECRET_KEY"] = "123456790"
    app.config["MONGODB_HOST"] = os.environ.get("MONGODB_URI")
    app.config["MONG_DBNAME"] = "test"
    db.init_app(app)
    return app
