VERSION = (0, 1, 0)


def get_version():
    """
    Returns a PEP 386-compliant version number from VERSION.
    """
    parts = 2 if VERSION[2] == 0 else 3
    main = '.'.join(str(x) for x in VERSION[:parts])
    return main

default_app_config = 'background_tasker.apps.BackgroundTasker'
