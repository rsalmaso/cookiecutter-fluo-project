import readenv.loads  # noqa: F401 isort:skip
import service_urls.patch  # noqa: F401 isort:skip

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{{ cookiecutter.project_name }}.settings")

application = get_asgi_application()