import os

from fluo.management.commands.serve import Command as BaseCommand


class Command(BaseCommand):
    def get_default_port(self):
        return os.environ.get('{{ cookiecutter.upper_case_app_name }}_DEFAULT_PORT', super().get_default_port())

    def get_default_addr(self):
        return os.environ.get('{{ cookiecutter.upper_case_app_name }}_DEFAULT_ADDR', super().get_default_addr())

    def get_default_addr_ipv6(self):
        return os.environ.get('{{ cookiecutter.upper_case_app_name }}_DEFAULT_ADDR6', super().get_default_addr_ipv6())
