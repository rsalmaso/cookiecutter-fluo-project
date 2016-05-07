{% if cookiecutter.use_python2 == "y" %}# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function, unicode_literals
{% endif %}from django.utils.translation import ugettext_lazy as _
from fluo.apps import FluoConfig as AppConfig


class {{ cookiecutter.camel_case_app_name }}Config(AppConfig):
    name = "{{ cookiecutter.project_name }}"
    verbose_name = _("{{ cookiecutter.camel_case_app_name }}")

    #def get_admin_site(self):
        #return super().get_admin_site()

    #def ready(self):
        #super().ready()
