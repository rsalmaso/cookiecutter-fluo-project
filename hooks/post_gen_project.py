# Copyright (C) 2007-2020, Raffaele Salmaso <raffaele@salmaso.org>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import contextlib
import glob
import os
import random
import shutil
import subprocess
import time

PYTHON = os.environ.get("PYTHON", "python3")
VENV_NAME = "{}.{}".format("{{ cookiecutter.project_dir }}", str(time.time()).split('.')[0])
VENV_PATH = f"/tmp/{VENV_NAME}"
VENV_PIP = f"{VENV_PATH}/bin/pip"
VENV_PYTHON = f"{VENV_PATH}/bin/python3"
PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)

@contextlib.contextmanager
def cd(VENV_PATH):
    cwd = os.getcwd()
    os.chdir(VENV_PATH)
    yield
    os.chdir(cwd)

def system(*args, **kwargs):
    env = kwargs.pop('env', None)
    return subprocess.call(list(args), env=env)

class Project:
    def mkdir(self, directory):
        system("mkdir", "-p", os.path.join(
            PROJECT_DIRECTORY,
            directory,
        ))

    def create_venv(self):
        system(
            PYTHON,
            "-m",
            "venv",
            VENV_PATH
        )
        system(
            VENV_PIP,
            "install",
            "--upgrade",
            "pip",
            "wheel",
            "setuptools",
            "pip-tools",
        )

    def install_libs(self):
        system(
            VENV_PYTHON,
            "-m",
            "piptools",
            "compile",
            "--annotation-style",
            "line"
        )
        system(
            VENV_PYTHON,
            "-m",
            "piptools",
            "sync",
        )

    def collectstatic(self):
        system(
            VENV_PYTHON,
            os.path.join(PROJECT_DIRECTORY, "manage.py"),
            "collectstatic",
            "--noinput",
        )

def get_random_string(length=50, allowed_chars="abcdefghijklmnopqrstuvwxyz0123456789!@#%^&*(-_=+)"):
    """
    Returns a securely generated random string.
    The default length of 12 with the a-z, A-Z, 0-9 character set returns
    a 71-bit value. log_2((26+26+10)^12) =~ 71 bits
    """
    #if not using_sysrandom:
        ## This is ugly, and a hack, but it makes things better than
        ## the alternative of predictability. This re-seeds the PRNG
        ## using a value that is hard for an attacker to predict, every
        ## time a random string is required. This may change the
        ## properties of the chosen random sequence slightly, but this
        ## is better than absolute predictability.
        #random.seed(
            #hashlib.sha256(
                #("%s%s%s" % (
                    #random.getstate(),
                    #time.time(),
                    #settings.SECRET_KEY)).encode('utf-8')
            #).digest())
    return "".join(random.choice(allowed_chars) for i in range(length))

def set_secret_key(setting_file_location):
    # Open locals.py
    with open(setting_file_location) as f:
        file_ = f.read()

    # Generate a SECRET_KEY that matches the Django standard
    SECRET_KEY = get_random_string()

    # Replace "CHANGEME!!!" with SECRET_KEY
    file_ = file_.replace("<%SECRET_KEY%>", SECRET_KEY, 1)

    # Write the results to the locals.py module
    with open(setting_file_location, 'w') as f:
        f.write(file_)

def make_secret_key(project_directory):
    """Generates and saves random secret key"""
    # Determine the local_setting_file_location
    set_secret_key(os.path.join(
        project_directory,
        "{{ cookiecutter.project_name }}",
        "conf",
        "local.py",
    ))

    set_secret_key(os.path.join(
        project_directory,
        "{{ cookiecutter.project_name }}",
        "conf",
        "base.py",
    ))

def remove_vuejs_files():
    path = os.path.join(
        PROJECT_DIRECTORY,
        "{{ cookiecutter.project_name }}",
        "static",
        "{{ cookiecutter.project_name }}",
        "libs",
        "vue",
    )
    if os.path.exists(path):
        shutil.rmtree(path)

def remove_postgresql_files():
    os.remove(os.path.join(PROJECT_DIRECTORY, "{{ cookiecutter.project_name }}", "migrations", "0001_initial.py"))

def remove_working_files():
    os.remove(os.path.join(PROJECT_DIRECTORY, "COPYING.py"))

def init():
    make_secret_key(PROJECT_DIRECTORY)

    project = Project()
    project.create_venv()
    project.install_libs()
    if '{{ cookiecutter.use_postgresql }}'.lower() == 'n':
        remove_postgresql_files()
    if '{{ cookiecutter.use_vuejs }}'.lower() == 'n':
        remove_vuejs_files()
    remove_working_files()
    project.collectstatic()

init()
