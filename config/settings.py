import os
from datetime import timedelta

SESSION_PERMANENT = False
SESSION_TYPE = "filesystem"
SECRET_KEY = os.environ.get("SECRET_KEY")
MONGODB_HOST = (
    os.environ.get("MONGODB_URI_DEV")
    if os.environ.get("FLASK_ENVIRONMENT") == "development"
    else os.environ.get("MONGODB_URI_PROD")
)
MONG_DBNAME = "test"
PERMANENT_SESSION_LIFETIME = timedelta(minutes=15)
MAIL_SERVER = "smtp.gmail.com"
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
