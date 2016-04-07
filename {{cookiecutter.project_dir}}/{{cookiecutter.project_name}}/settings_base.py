"""
Django settings for {{ cookiecutter.project_name }} project.
"""

import errno
import getpass
import os
from django.core.urlresolvers import reverse_lazy

PROJECT_NAME = "{{ cookiecutter.project_name }}"
PROJECT_PATH = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]

def rel(*args):
    return os.path.normpath(os.path.join(PROJECT_PATH, *args))
def mkdir(dir):
    try:
        os.makedirs(dir)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise e

LIB_DIR = rel("lib")
def lib_rel(*args):
    return os.path.normpath(os.path.join(LIB_DIR, *args))
LOG_DIR = rel("log")
def log_rel(*args):
    return os.path.normpath(os.path.join(LOG_DIR, *args))
CONF_DIR = rel("conf")
def conf_rel(*args):
    return os.path.normpath(os.path.join(CONF_DIR, *args))
TMP_DIR = rel("tmp")
def tmp_rel(*args):
    return os.path.normpath(os.path.join(TMP_DIR, *args))
# make sure log and tmp dirs exist
mkdir(LOG_DIR)
mkdir(TMP_DIR)

_ = lambda s: s
#LANGUAGES = [
    #("it", _("Italian")),
    #("en", _("English")),
#]

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ADMINS = [
    # ('Your Name', 'your_email@example.com'),
]

MANAGERS = ADMINS

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

DATABASES = {
    "default": {
        "ENGINE": os.environ.get("DATABASE_ENGINE", "django.db.backends.postgresql"),
        "NAME": os.environ.get("DATABASE_NAME", "{{ cookiecutter.project_name }}"),
        "USER": os.environ.get("DATABASE_USER", getpass.getuser()),
        "PASSWORD": os.environ.get("DATABASE_PASSWORD", ""),
        "HOST": os.environ.get("DATABASE_HOST", ""),
        "PORT": os.environ.get("DATABASE_PORT", "5432"),

        #"ENGINE": os.environ.get("DATABASE_ENGINE", "django.db.backends.sqlite3"),
        #"NAME": os.environ.get("DATABASE_NAME", rel("{{ cookiecutter.project_name }}.db")),
        #"PASSWORD": os.environ.get("DATABASE_PASSWORD", ""),
        #"USER": os.environ.get("DATABASE_USER", ""),
        #"HOST": os.environ.get("DATABASE_HOST", ""),
        #"PORT": os.environ.get("DATABASE_PORT", ""),

        #"ENGINE": os.environ.get("DATABASE_ENGINE", "django.db.backends.mysql"),
        #"NAME": os.environ.get("DATABASE_NAME", "{{ cookiecutter.project_name }}")),
        #"PASSWORD": os.environ.get("DATABASE_PASSWORD", ""),
        #"USER": os.environ.get("DATABASE_USER", ""),
        #"HOST": os.environ.get("DATABASE_HOST", ""),
        #"PORT": os.environ.get("DATABASE_PORT", ""),
        #"OPTIONS": {"init_command": "SET storage_engine=INNODB"},
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = "Europe/Rome"

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = "en-us"

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True
#LOCALE_PATHS = []

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = rel("media")
mkdir(MEDIA_ROOT)

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = "/media/"

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = rel("static")
mkdir(STATIC_ROOT)

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = "/static/"

# Additional locations of static files
STATICFILES_DIRS = [
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.

    #lib_rel('django', 'contrib', 'admin', 'static'),
    #lib_rel('fluo', 'static'),
]

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    #"django.contrib.staticfiles.finders.DefaultStorageFinder",
]

#STATICFILES_STORAGE = "django.contrib.staticfiles.storage.CachedStaticFilesStorage"

# SECURITY WARNING: keep the secret key used in production secret!
# Make this unique, and don't share it with anybody.
SECRET_KEY = os.environ.get("SECRET_KEY", "<%SECRET_KEY%>")

TEMPLATES = [{
    "BACKEND": "django.template.backends.django.DjangoTemplates",
    "DIRS": [
        # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
        # Always use forward slashes, even on Windows.
        # Don't forget to use absolute paths, not relative paths.

        #rel("templates"),
    ],
    "APP_DIRS": True,
    "OPTIONS": {
        "context_processors": [
            "django.template.context_processors.debug",
            "django.template.context_processors.request",
            "django.contrib.auth.context_processors.auth",
            "django.contrib.messages.context_processors.messages",

            "django.core.context_processors.i18n",
            "django.core.context_processors.request",
            "django.core.context_processors.tz",
            #"django.core.context_processors.csrf",
            #"fluo.context_processors.media",
            #"fluo.context_processors.static",
        ],
        #"loaders": [
            #"django.template.loaders.filesystem.Loader",
            #"django.template.loaders.app_directories.Loader",
        #],
    },
}]

MIDDLEWARE_CLASSES = [
    #"django.middleware.cache.UpdateCacheMiddleware", # enable cache
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.auth.middleware.SessionAuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    #"django.middleware.http.ConditionalGetMiddleware",
    #"django.middleware.gzip.GZipMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    #"django.middleware.cache.FetchFromCacheMiddleware", # enable cache
]
INTERNAL_IPS = ["127.0.0.1"]

ROOT_URLCONF = "{{ cookiecutter.project_name }}.urls"
LOGIN_URL = reverse_lazy("login")
LOGOUT_URL = reverse_lazy("logout")
LOGIN_REDIRECT_URL = "/" #"/accounts/profile/"

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = os.environ.get("WSGI_APPLICATION", "{{ cookiecutter.project_name }}.wsgi.application")

INSTALLED_APPS = [
    "django.contrib.auth.apps.AuthConfig",
    "django.contrib.contenttypes.apps.ContentTypesConfig",
    "django.contrib.sessions.apps.SessionsConfig",
    "django.contrib.sites.apps.SitesConfig",
    "django.contrib.messages.apps.MessagesConfig",
    "django.contrib.staticfiles.apps.StaticFilesConfig",
    "django.contrib.admin.apps.AdminConfig",
    "fluo.apps.FluoConfig",
    "{{ cookiecutter.project_name }}.apps.{{ cookiecutter.camel_case_app_name }}Config",
]

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    "version": 1,
    "disable_existing_loggers": True,
    "formatters": {
        "verbose": {
            "format": "%(asctime)s - %(process)5d %(pathname)s::%(funcName)s[%(lineno)d]: %(levelname)s %(message)s",
        },
        "simple": {
            "format": "[%(asctime)s] %(levelname)s %(message)s",
        },
    },
    "filters": {
        "require_debug_false": {
            "()": "django.utils.log.CallbackFilter",
            "callback": lambda r: not DEBUG,
        },
       #"special": {
           #"()": "{{ cookiecutter.project_name }}.logging.SpecialFilter",
           #"foo": "bar",
       #},
    },
    "handlers": {
        "null": {
            "level": "DEBUG",
            "class": "logging.NullHandler",
        },
        "console":{
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
        "file":{
            "level": "INFO",
            "class": "logging.handlers.TimedRotatingFileHandler",
            "formatter": "verbose",
            "filename": log_rel("{{ cookiecutter.project_name }}-info.log"),
            "when": "D",
            "interval": 7,
            "backupCount": 4,
            # rotate every 7 days, keep 4 old copies
        },
        "error_file":{
            "level": "ERROR",
            "class": "logging.handlers.TimedRotatingFileHandler",
            "formatter": "verbose",
            "filename": log_rel("{{ cookiecutter.project_name }}-error.log"),
            "when": "D",
            "interval": 7,
            "backupCount": 4,
            # rotate every 7 days, keep 4 old copies
        },
        "mail_admins": {
            "level": "ERROR",
            "class": "django.utils.log.AdminEmailHandler",
            "include_html": True,
            #"filters": ["special"]
            "filters": ["require_debug_false"],
        },
    },
    "loggers": {
        "django": {
            # django is the catch-all logger. No messages are posted directly to this logger.
            "handlers": ["null", "error_file"],
            "propagate": True,
            "level":"INFO",
        },
        "django.request": {
            # Log messages related to the handling of requests. 5XX responses are
            # raised as ERROR messages; 4XX responses are raised as WARNING messages.
            "handlers": ["error_file", "mail_admins"],
            "level": "ERROR",
            "propagate": False,
        },
        "{{ cookiecutter.project_name }}": {
            "handlers": ["console", "file", "error_file", "mail_admins"],
            "level": "INFO",
            #"filters": ["special"]
        },
    },
}

### Cache
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

#DEFAULT_FROM_EMAIL = "webmaster@localhost"
#EMAIL_SUBJECT_PREFIX = "[Django] "
#SERVER_EMAIL = "root@localhost"
EMAIL_BACKEND = os.environ.get("EMAIL_BACKEND", "django.core.mail.backends.console.EmailBackend")



#######################
# Password validation #
#######################

AUTH_PASSWORD_VALIDATORS = [
    #{
        #'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    #},
    #{
        #'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    #},
    #{
        #'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    #},
    #{
        #'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    #},
]

SILENCED_SYSTEM_CHECKS = [
]

########################
# DJANGO DEBUG TOOLBAR #
########################

DEBUG_TOOLBAR_CONFIG = {
    "INTERCEPT_REDIRECTS": False,
    "HIDE_DJANGO_SQL": False,
    "ENABLE_STACKTRACES" : True,
}
