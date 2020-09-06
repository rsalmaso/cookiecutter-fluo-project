from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "this command does nothing"

    def handle(self, *args, **options):
        pass
