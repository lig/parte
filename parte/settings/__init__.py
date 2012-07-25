from dist import *
try:
    from local import *
except ImportError:
    from local_sample import *
    from warnings import warn
    warn(
        'Local settings not found (settings/local.py).'
        'Using local_sample.py instead.')
