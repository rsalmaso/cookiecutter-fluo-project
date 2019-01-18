"""
Django settings for {{ cookiecutter.project_name }} project.
"""

import getpass
import os
# from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

PROJECT_NAME = "{{ cookiecutter.project_name }}"
PROJECT_PATH = os.path.split(os.path.split(os.path.split(os.path.realpath(__file__))[0])[0])[0]


def rel(*args):
    return os.path.normpath(os.path.join(PROJECT_PATH, *args))


LIB_DIR = os.environ.get("LIB_DIR", rel("lib"))


def lib_rel(*args):
    return os.path.normpath(os.path.join(LIB_DIR, *args))


LOG_DIR = os.environ.get("LOG_DIR", rel("log"))


def log_rel(*args):
    return os.path.normpath(os.path.join(LOG_DIR, *args))


CONF_DIR = os.environ.get("CONF_DIR", rel("conf"))


def conf_rel(*args):
    return os.path.normpath(os.path.join(CONF_DIR, *args))


TMP_DIR = os.environ.get("TMP_DIR", rel("tmp"))


def tmp_rel(*args):
    return os.path.normpath(os.path.join(TMP_DIR, *args))


LANGUAGES = [
    ("it", _("Italian")),
    ("en", _("English")),
]

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
    "default": os.environ.get("DATABASES_DEFAULT", os.environ.get("DATABASE_URL", f"postgres://{getpass.getuser()}:@:5432/{{ cookiecutter.db_name }}")),
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = os.environ.get("TIME_ZONE", "Europe/Rome")

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = os.environ.get("LANGUAGE_CODE", "en")

SITE_ID = 1

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.environ.get("MEDIA_ROOT", rel("media"))

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = "/media/"

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.environ.get("STATIC_ROOT", rel("static"))

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = "/static/"

# Additional locations of static files
STATICFILES_DIRS = [
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.

    # lib_rel('django', 'contrib', 'admin', 'static'),
    # lib_rel('fluo', 'static'),
]

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    # "django.contrib.staticfiles.finders.DefaultStorageFinder",
]

STATICFILES_STORAGE = os.environ.get("STATICFILES_STORAGE", {% if cookiecutter.use_whitenoise == "y" %}"whitenoise.storage.CompressedManifestStaticFilesStorage"{% else %}"django.contrib.staticfiles.storage.ManifestStaticFilesStorage"{% endif %})

# SECURITY WARNING: keep the secret key used in production secret!
# Make this unique, and don't share it with anybody.
SECRET_KEY = os.environ.get("SECRET_KEY", "<%SECRET_KEY%>")

TEMPLATES = [{
    "BACKEND": "django.template.backends.django.DjangoTemplates",
    "DIRS": [
        # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
        # Always use forward slashes, even on Windows.
        # Don't forget to use absolute paths, not relative paths.

        # rel("templates"),
    ],
    "APP_DIRS": True,
    "OPTIONS": {
        "context_processors": [
            #"django.template.context_processors.csrf",
            "django.template.context_processors.debug",
            "django.template.context_processors.i18n",
            "django.template.context_processors.request",
            "django.template.context_processors.tz",
            "django.contrib.auth.context_processors.auth",
            "django.contrib.messages.context_processors.messages",{% if cookiecutter.project_type == "django-cms" %}
            "cms.context_processors.cms_settings",{% endif %}{% if cookiecutter.use_sekizai == "y" or cookiecutter.project_type == "django-cms" %}
            "sekizai.context_processors.sekizai",{% endif %}
        ],
        "builtins": [
            "fluo.templatetags.backports",
        ],
    },
}]

MIDDLEWARE = [
    # "django.middleware.cache.UpdateCacheMiddleware",  # enable cache{% if cookiecutter.project_type == "django-cms" %}
    "cms.middleware.utils.ApphookReloadMiddleware",{% endif %}
    "django.middleware.security.SecurityMiddleware",{% if cookiecutter.use_whitenoise == "y" %}
    "whitenoise.middleware.WhiteNoiseMiddleware",{% endif %}
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    # "django.middleware.http.ConditionalGetMiddleware",
    # "django.middleware.gzip.GZipMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",{% if cookiecutter.project_type == "django-cms" %}
    "cms.middleware.user.CurrentUserMiddleware",
    "cms.middleware.page.CurrentPageMiddleware",
    "cms.middleware.toolbar.ToolbarMiddleware",
    "cms.middleware.language.LanguageCookieMiddleware",{% endif %}
    # "django.middleware.cache.FetchFromCacheMiddleware",  # enable cache
]
INTERNAL_IPS = ["127.0.0.1"]

ROOT_URLCONF = os.environ.get("ROOT_URLCONF", "{{ cookiecutter.project_name }}.urls")
# LOGIN_URL = reverse_lazy("login")
# LOGOUT_URL = reverse_lazy("logout")
# LOGIN_REDIRECT_URL = "/" #"/accounts/profile/"
AUTH_USER_MODEL = "auth.User"

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = os.environ.get("WSGI_APPLICATION", "{{ cookiecutter.project_name }}.wsgi.application")

INSTALLED_APPS = [
    "{{ cookiecutter.project_name }}.apps.{{ cookiecutter.camel_case_app_name }}Config",

    {% if cookiecutter.use_postgresql == "y" %}"django.contrib.postgres.apps.PostgresConfig",
    {% endif %}"django.contrib.auth.apps.AuthConfig",
    "django.contrib.contenttypes.apps.ContentTypesConfig",
    "django.contrib.sessions.apps.SessionsConfig",
    "django.contrib.sites.apps.SitesConfig",
    "django.contrib.messages.apps.MessagesConfig",{% if cookiecutter.use_whitenoise == "y" %}
    "whitenoise.runserver_nostatic",{% endif %}
    "{{ cookiecutter.project_name }}.apps.StaticFilesConfig",
    "{{ cookiecutter.project_name }}.apps.AdminConfig",
    "fluo.apps.FluoConfig",{% if cookiecutter.use_sorl_thumbnail == "y" %}
    "sorl.thumbnail",{% endif %}{% if cookiecutter.use_djangorestframework == "y" %}

    "rest_framework",
    "rest_framework.authtoken",{% endif %}{% if cookiecutter.use_sekizai == "y" or cookiecutter.project_type == "django-cms" %}

    "{{ cookiecutter.project_name }}.apps.ClassyTagsConfig",
    "{{ cookiecutter.project_name }}.apps.SekizaiConfig",{% endif %}{% if cookiecutter.use_widget_tweaks == "y" or cookiecutter.project_type == "django-cms" %}
    "{{ cookiecutter.project_name }}.apps.WidgetTweaksConfig",{% endif %}{% if cookiecutter.project_type == "django-cms" %}

    "mptt",
    "treebeard",
    "djangocms_text_ckeditor", # note this needs to be above the "cms" entry
    "menus.apps.MenusConfig",
    "easy_thumbnails",
    "formtools",

    "cms.apps.CMSConfig",

    "djangocms_column",
    "djangocms_file",
    "djangocms_googlemap",
    "djangocms_link",
    "djangocms_picture",
    "djangocms_style",
    "djangocms_teaser",
    "djangocms_video",

    "filer",{% endif %}{% if cookiecutter.use_cookielaw == "y" %}
    "legal.apps.LegalConfig",{% endif %}
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
        "django.server": {
            "()": "django.utils.log.ServerFormatter",
            "format": "[%(server_time)s] %(message)s",
        },
    },
    "filters": {
        "require_debug_false": {
            "()": "django.utils.log.CallbackFilter",
            "callback": lambda r: not DEBUG,
        },
        # "special": {
        #    "()": "{{ cookiecutter.project_name }}.logging.SpecialFilter",
        #    "foo": "bar",
        # },
    },
    "handlers": {
        "null": {
            "level": "DEBUG",
            "class": "logging.NullHandler",
        },
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
        "file": {
            "level": "INFO",
            "class": "logging.handlers.TimedRotatingFileHandler",
            "formatter": "verbose",
            "filename": log_rel("{{ cookiecutter.project_name }}-info.log"),
            "when": "D",
            "interval": 7,
            "backupCount": 4,
            "delay": True,
            # rotate every 7 days, keep 4 old copies
        },
        "error_file": {
            "level": "ERROR",
            "class": "logging.handlers.TimedRotatingFileHandler",
            "formatter": "verbose",
            "filename": log_rel("{{ cookiecutter.project_name }}-error.log"),
            "when": "D",
            "interval": 7,
            "backupCount": 4,
            "delay": True,
            # rotate every 7 days, keep 4 old copies
        },
        "mail_admins": {
            "level": "ERROR",
            "class": "django.utils.log.AdminEmailHandler",
            "include_html": True,
            # "filters": ["special"]
            "filters": ["require_debug_false"],
        },
        "django.server": {
            "level": "INFO",
            "class": "logging.StreamHandler",
            "formatter": "django.server",
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
        "django.server": {
            "handlers": ["django.server"],
            "level": "INFO",
            "propagate": False,
        },
        "gunicorn.error": {
            "level": "DEBUG",
            "handlers": ["console"],
            "propagate": True
        },
        "gunicorn.access": {
            "level": "DEBUG",
            "handlers": ["console"],
            "propagate": False
        },
        "{{ cookiecutter.project_name }}": {
            "handlers": ["console", "file", "error_file", "mail_admins"],
            "level": "INFO",
            # "filters": ["special"]
        },
    },
}

#########
# Cache #
#########
CACHES = {
    "default": "dummy://"
}
# CACHE_MIDDLEWARE_KEY_PREFIX = ""
# CACHE_MIDDLEWARE_SECONDS = 600
# CACHE_MIDDLEWARE_ALIAS = "default"

##########
# EMAILS #
##########

# DEFAULT_FROM_EMAIL = "webmaster@localhost"
# EMAIL_SUBJECT_PREFIX = "[Django] "
# SERVER_EMAIL = "root@localhost"
EMAIL_BACKEND = os.environ.get("EMAIL_BACKEND", f"file://{rel('emails')}")


{% if cookiecutter.project_type == "django-cms" %}##############
# DJANGO CMS #
##############

THUMBNAIL_PROCESSORS = (
    "easy_thumbnails.processors.colorspace",
    "easy_thumbnails.processors.autocrop",
    # "easy_thumbnails.processors.scale_and_crop",
    "filer.thumbnail_processors.scale_and_crop_with_subject_location",
    "easy_thumbnails.processors.filters",
)
THUMBNAIL_MEDIA_ROOT = os.environ.get("THUMBNAIL_MEDIA_ROOT", os.path.join(MEDIA_ROOT, "cache"))
THUMBNAIL_MEDIA_URL = MEDIA_URL + "cache/"
# THUMBNAIL_BASEDIR = "cache"

CMS_TEMPLATES = [
    ("{{ cookiecutter.project_name }}/index.html", _("Home Page (T1)")),
]
CMS_PLACEHOLDER_CONF = {
}

CMS_PERMISSION = False
# CMS_MODERATOR = True
CMS_URL_OVERWRITE = True
CMS_MENU_TITLE_OVERWRITE = True
CMS_SEO_FIELDS = True
CMS_REDIRECTS = True
CMS_LANGUAGES = {
    1: [
        {
            "code": lang[0],
            "name": lang[1],
            "fallbacks": ["en"],
            "public": True,
        } for lang in LANGUAGES
    ],
    "default": {
        "fallbacks": [lang[0] for lang in LANGUAGES],
        "redirect_on_fallback": True,
        "public": True,
        "hide_untranslated": False,
    }
}
CMS_SHOW_START_DATE = True
CMS_SHOW_END_DATE = True

{% endif %}
#######################
# Password validation #
#######################

AUTH_PASSWORD_VALIDATORS = [
    # {
    #     "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    # },
    # {
    #     "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    # },
    # {
    #     "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    # },
    # {
    #     "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    # },
]
{% if cookiecutter.use_djangorestframework == "y" %}
#########################
# DJANGO REST FRAMEWORK #
#########################

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        # "rest_framework.authentication.BasicAuthentication",  # only for https
        "rest_framework.authentication.SessionAuthentication",
        # "rest_framework.authentication.TokenAuthentication",  # only for https
    ),
    "DEFAULT_RENDERER_CLASSES": (
        "rest_framework.renderers.JSONRenderer",
        # "rest_framework.renderers.TemplateHTMLRenderer",
        # "rest_framework.renderers.BrowsableAPIRenderer",
    ),
    "DEFAULT_PARSER_CLASSES": (
        "rest_framework.parsers.JSONParser",
        "rest_framework.parsers.FormParser",
        "rest_framework.parsers.MultiPartParser",
    ),
}{% endif %}

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
