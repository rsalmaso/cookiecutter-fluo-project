import readenv.loads  # noqa: F401 isort:skip
import service_urls.patch  # noqa: F401 isort:skip

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{{ cookiecutter.project_name }}.settings")

application = get_wsgi_application()
