from .base import *

ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "*").split(",")
DEBUG = os.environ.get("DEBUG", "true").lower() in ("true", "1")
SECRET_KEY = os.environ.get("SECRET_KEY", "<%SECRET_KEY%>")
