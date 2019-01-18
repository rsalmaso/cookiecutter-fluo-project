import os

DIRS = ("LOG_DIR", "CONF_DIR", "TMP_DIR", "MEDIA_ROOT", "STATIC_ROOT", "EMAIL_FILE_PATH"{% if cookiecutter.use_sorl_thumbnail == "y" %}, "THUMBNAIL_MEDIA_ROOT"{% endif %})


def check_dirs(app_configs, **kwargs):
    """make sure these dirs exist"""
    from django.conf import settings
    for name in DIRS:
        path = getattr(settings, name, None)
        if path:
            os.makedirs(path, exist_ok=True)
    return []
