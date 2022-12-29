from dotenv import load_dotenv
from routes.index import index
import os
def create_app(app):
    load_dotenv('.env')
    app.register_blueprint(index,url_prefix='/')
    return app