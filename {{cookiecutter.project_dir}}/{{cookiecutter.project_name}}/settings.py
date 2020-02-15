try:
    from .conf.local import *
except ImportError:
    from .conf.base import *


# make sure these dirs exist
for setting in ("LOG_DIR", "CONF_DIR", "TMP_DIR", "MEDIA_ROOT", "STATIC_ROOT", "EMAIL_FILE_PATH"{% if cookiecutter.use_sorl_thumbnail == "y" %}, "THUMBNAIL_MEDIA_ROOT"{% endif %}):
    path = globals().get(setting, None)
    if path:
        os.makedirs(path, exist_ok=True)
