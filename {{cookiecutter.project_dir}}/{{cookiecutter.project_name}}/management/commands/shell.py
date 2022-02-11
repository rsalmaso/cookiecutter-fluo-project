from django.core.management.commands.shell import Command as BaseCommand


class Command(BaseCommand):
    def ipython(self, options):
        from IPython import start_ipython

        start_ipython(argv=["--TerminalInteractiveShell.autoformatter=None"])
