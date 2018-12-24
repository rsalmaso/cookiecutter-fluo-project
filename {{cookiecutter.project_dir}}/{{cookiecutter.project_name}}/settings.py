import service_urls

try:
    from .conf.local import *
except ImportError:
    from .conf.base import *

try:
    DATABASES
except:
    pass
else:
    DATABASES = service_urls.db.parse(DATABASES)

try:
    CACHES
except:
    pass
else:
    CACHES = service_urls.cache.parse(CACHES)

try:
    EMAIL_BACKEND
except:
    pass
else:
    if service_urls.email.validate(EMAIL_BACKEND):
        for k, v in service_urls.email.parse(EMAIL_BACKEND).items():
            setting = 'EMAIL_{}'.format('BACKEND' if k == 'ENGINE' else k)
            globals()[setting] = v

try:
    EMAIL_FILE_PATH
except:
    pass
else:
    if (EMAIL_FILE_PATH):
        mkdir(EMAIL_FILE_PATH)
