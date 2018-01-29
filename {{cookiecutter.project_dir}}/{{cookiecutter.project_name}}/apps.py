from django.apps import AppConfig
from django.utils.module_loading import import_module
from django.utils.translation import gettext_lazy as _
from fluo.apps import FluoAdminConfig


class {{ cookiecutter.camel_case_app_name }}AdminConfig(FluoAdminConfig):
    default_site = "{{ cookiecutter.project_name }}.admin.sites.AdminSite"

    def ready(self):
        super().ready()
        import_module("{{ cookiecutter.project_name }}.admin.views")


class {{ cookiecutter.camel_case_app_name }}Config(AppConfig):
    name = "{{ cookiecutter.project_name }}"
    verbose_name = _("{{ cookiecutter.camel_case_app_name }}")


class ClassyTagsConfig(AppConfig):
    name = "classytags"
    verbose_name = _("Classy Tags")


class SekizaiConfig(AppConfig):
    name = "sekizai"
    verbose_name = _("Sekizai")


class WidgetTweaksConfig(AppConfig):
    name = "widget_tweaks"
    verbose_name = _("Widget Tweaks")
