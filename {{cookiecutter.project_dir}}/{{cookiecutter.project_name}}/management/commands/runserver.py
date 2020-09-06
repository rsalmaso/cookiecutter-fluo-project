import os

from whitenoise.runserver_nostatic.management.commands.runserver import Command as BaseCommand


class Command(BaseCommand):
    @property
    def default_port(self):
        return os.environ.get("DJANGO_DEFAULT_PORT", super().default_port)

    @property
    def default_addr(self):
        return os.environ.get("DJANGO_DEFAULT_ADDR", super().default_addr)

    @property
    def default_addr_ipv6(self):
        return os.environ.get("DJANGO_DEFAULT_ADDR6", super().default_addr_ipv6)
