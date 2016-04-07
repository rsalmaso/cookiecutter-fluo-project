#!/usr/bin/env python3
import os, sys

# PATH is the absolute path leading to parent directory
PATH = os.path.dirname(os.path.realpath(__file__))
def add(path):
    PATH_DIR = os.path.join(PATH, path)
    if PATH_DIR not in sys.path:
        sys.path.insert(0, PATH_DIR)
add('lib')


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{{ cookiecutter.project_name }}.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
