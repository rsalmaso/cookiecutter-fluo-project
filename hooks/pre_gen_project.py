import cookiecutter

project_name = "{{ cookiecutter.project_name }}"

if hasattr(project_name, "isidentifier"):
    assert project_name.isidentifier(), "Project slug should be valid Python identifier!"

assert cookiecutter.__version__ >= "1.4.0", "Please upgrade your Cookiecutter installation"
