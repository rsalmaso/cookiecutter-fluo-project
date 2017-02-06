from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _
from fluo.apps import FluoAdminConfig


class {{ cookiecutter.camel_case_app_name }}AdminConfig(FluoAdminConfig):
    default_site = "{{ cookiecutter.project_name }}.admin.sites.AdminSite"


class {{ cookiecutter.camel_case_app_name }}Config(AppConfig):
    name = "{{ cookiecutter.project_name }}"
    verbose_name = _("{{ cookiecutter.camel_case_app_name }}")
