"""
WSGI config for www project.

This module contains the WSGI application used by Django's development server
and any production WSGI deployments. It should expose a module-level variable
named ``application``. Django's ``runserver`` and ``runfcgi`` commands discover
this application via the ``WSGI_APPLICATION`` setting.

Usually you will have the standard Django WSGI application here, but it also
might make sense to replace the whole Django WSGI application with a custom one
that later delegates to the Django one. For example, you could introduce WSGI
middleware here, or combine a Django application with an application of another
framework.

"""

import os
import sys

# PATH is the absolute path leading to parent directory
PROJECT_PATH = os.path.split(os.path.realpath(__file__))[0]
PATH = os.path.split(PROJECT_PATH)[0]
LIB_DIR = os.path.join(PATH, 'lib')

if LIB_DIR not in sys.path:
    sys.path.insert(0, LIB_DIR)
if PATH not in sys.path:
    sys.path.insert(0, PATH)

# remove current path
try:
    sys.path.remove(PROJECT_PATH)
except ValueError:
    pass

import service_urls.patch  # noqa: F401 isort:skip

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{{ cookiecutter.project_name }}.settings")

# This application object is used by any WSGI server configured to use this
# file. This includes Django's development server, if the WSGI_APPLICATION
# setting points here.
from django.core.wsgi import get_wsgi_application  # isort:skip
_application = get_wsgi_application()

def application(environ, start_response):
    if environ['wsgi.url_scheme'] == 'https':
        environ['HTTPS'] = 'on'
    return _application(environ, start_response)

# Apply WSGI middleware here.
# from helloworld.wsgi import HelloWorldApplication
# application = HelloWorldApplication(application)
