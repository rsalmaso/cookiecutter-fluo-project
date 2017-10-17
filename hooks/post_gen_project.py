# Copyright (C) 2007-2016, Raffaele Salmaso <raffaele@salmaso.org>
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
import os
import random
import shutil
import subprocess

import pip

PYTHON = "python3"
PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)
LIB_DIR = os.path.join(PROJECT_DIRECTORY, "lib")
PATCHES_DIR = os.path.join(PROJECT_DIRECTORY, "_patches")

@contextlib.contextmanager
def cd(path):
    cwd = os.getcwd()
    os.chdir(path)
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

    def install_libs(self):
        self.mkdir("lib")
        cmd = [
            "install",
            "--target={}".format(LIB_DIR),
            "-r", "requirements.txt",
        ]
        pip.main(cmd)

    def collectstatic(self):
        system(
            "/usr/bin/env",
            PYTHON,
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
        "settings.py",
    ))

    set_secret_key(os.path.join(
        project_directory,
        "{{ cookiecutter.project_name }}",
        "settings_base.py",
    ))

def apply_patches():
    cwd = os.getcwd()
    os.chdir(LIB_DIR)
    libs = [lib for lib in os.listdir(LIB_DIR) if os.path.isdir(lib) and not lib.endswith(".dist-info") and lib != "__pycache__"]
    patches = [patch for patch in os.listdir(PATCHES_DIR) if patch.endswith(".diff")]
    for patch in patches:
        lib = patch.split(".")[0]
        if lib in libs:
            os.chdir(os.path.join(LIB_DIR, lib))
            system("patch", "-p1", "-i", os.path.join(PATCHES_DIR, patch))
    os.chdir(cwd)

def cleanup_patches():
    if os.path.exists(PATCHES_DIR):
        shutil.rmtree(PATCHES_DIR)

def remove_postgresql_files():
    os.remove(os.path.join(PROJECT_DIRECTORY, "{{ cookiecutter.project_name }}", "migrations", "0001_initial.py"))

def init():
    make_secret_key(PROJECT_DIRECTORY)

    project = Project()
    project.install_libs()
    apply_patches()
    cleanup_patches()
    if '{{ cookiecutter.use_postgresql }}'.lower() == 'n':
        remove_postgresql_files()
    project.collectstatic()

init()
