import os

SESSION_PERMANENT = False
SESSION_TYPE = "filesystem"
SECRET_KEY = os.environ.get("SECRET_KEY")
MONGODB_HOST = os.environ.get("MONGODB_URI")
MONG_DBNAME = "test"
