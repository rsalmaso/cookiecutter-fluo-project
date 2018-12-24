import getpass
import os
import socket
from django.utils.translation import gettext_lazy as _
from .base import *

ADMINS = [
    # ("Your Name", "your_email@example.com"),
]
#ALLOWED_HOSTS = ["*"]

DEBUG = True

############
# DATABASE #
############

host = socket.gethostbyaddr(socket.gethostname())[0]
if host == "vagrant":
    pass
#elif host == "myhost":
    #DATABASES["default"].update({
        #"ENGINE": os.environ.get("DATABASE_ENGINE", "django.db.backends.postgresql"),
        #"NAME": os.environ.get("DATABASE_NAME", "{{ cookiecutter.db_name }}"),
        #"USER": os.environ.get("DATABASE_USER", getpass.getuser()),
        #"PASSWORD": os.environ.get("DATABASE_PASSWORD", ""),
        #"HOST": os.environ.get("DATABASE_HOST", ""),
        #"PORT": os.environ.get("DATABASE_PORT", "5432"),
    #})
else:
    # use default values defined in base.py
    pass


#########
# CACHE #
#########

#CACHES = {
    ## dummy backend
    #"default": {
        #"BACKEND": "django.core.cache.backends.dummy.DummyCache",
        #"LOCATION": "",
    #},
    ## filesystem based
    #"default": {
        #"BACKEND": "django.core.cache.backends.filebased.FileBasedCache",
        #"LOCATION": base_rel("tmp"),
    #},
    #CACHES = {
        #"default": {
            #"BACKEND": "django.core.cache.backends.memcached.MemcachedCache",
            #"LOCATION": "127.0.0.1:11211",
            #"LOCATION": "unix:/tmp/memcached.sock",
            #"LOCATION": [
                #"172.19.26.240:11211",
                #"172.19.26.242:11211",
            #],
        #},
    #},
    ## memory based
    #"default": {
        #"BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        #"LOCATION": "",
    #},
#}
#CACHE_MIDDLEWARE_KEY_PREFIX = ""
#CACHE_MIDDLEWARE_SECONDS = 600
#CACHE_MIDDLEWARE_ALIAS = "default"

#########
# EMAIL #
#########

#DEFAULT_FROM_EMAIL = "webmaster@localhost"
#EMAIL_SUBJECT_PREFIX = "[Django] "
#SERVER_EMAIL = "root@localhost"

# custom smtp account
#EMAIL_HOST = "localhost"
#EMAIL_PORT = 25
#EMAIL_HOST_USER = ""
#EMAIL_HOST_PASSWORD = ""
#EMAIL_USE_TLS = False

# use gmail account
#EMAIL_HOST = "smtp.gmail.com"
#EMAIL_PORT = 587
#EMAIL_HOST_USER = ""
#EMAIL_HOST_PASSWORD = ""
#EMAIL_USE_TLS = True

# custom email backend
# Don"t really send email, but print on console
EMAIL_BACKEND = os.environ.get("EMAIL_BACKEND", "django.core.mail.backends.console.EmailBackend")
#EMAIL_BACKEND = os.environ.get("EMAIL_BACKEND", "django.core.mail.backends.smtp.EmailBackend")
# Send email to
#EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

#################
# DEBUG TOOLBAR #
#################
#INTERNAL_IPS = ("127.0.0.1",)
#FORCE_DEBUG_TOOLBAR = False
