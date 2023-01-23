import os
from datetime import timedelta

SESSION_PERMANENT = False
SESSION_TYPE = "filesystem"
SECRET_KEY = os.environ.get("SECRET_KEY")
MONGODB_HOST = os.environ.get("MONGODB_URI")
MONG_DBNAME = "test"
PERMANENT_SESSION_LIFETIME = timedelta(minutes=15)
MAIL_SERVER = "smtp.gmail.com"
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
