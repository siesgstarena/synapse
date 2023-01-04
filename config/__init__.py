from dotenv import load_dotenv
load_dotenv('.env')
from routes.index import index
from . import firebase

def create_app(app):
    app.register_blueprint(index,url_prefix='/')
    return app