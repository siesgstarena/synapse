from routes.index import index

from db.mongo import init_mongo

# pylint: disable=unused-import
# flake8: noqa
from . import firebase


def create_app(app):
    app = init_mongo(app)
    app.register_blueprint(index, url_prefix="/")
    return app
