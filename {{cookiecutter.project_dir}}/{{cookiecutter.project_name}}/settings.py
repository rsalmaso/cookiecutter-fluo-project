try:
    from .conf.local import *
except ImportError:
    from .conf.base import *
