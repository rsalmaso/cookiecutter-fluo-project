from django.utils.translation import ugettext_lazy as _
from fluo.apps import FluoConfig as AppConfig


class {{ cookiecutter.camel_case_app_name }}Config(AppConfig):
    name = "{{ cookiecutter.project_name }}"
    verbose_name = _("{{ cookiecutter.camel_case_app_name }}")

    #def get_admin_site(self):
        #return super().get_admin_site()

    #def ready(self):
        #super().ready()
