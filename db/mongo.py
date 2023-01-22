from . import db


def init_mongo(app):
    db.init_app(app)
    return app
