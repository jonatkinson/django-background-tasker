from functools import wraps

import zmq
from .conf import settings
from .context import context


def task(func):
    """
    The task decorator that adds an ".aync" attribute to a function
    which when called will farm the process off to the background tasker
    """
    pusher = context.socket(zmq.PUSH)
    pusher.connect(settings.BACKGROUND_TASKER_URL)

    @wraps(func)
    def _async(*args, **kwargs):
        if settings.BACKGROUND_TASKER_ALWAYS_EAGER:
            func(*args, **kwargs)
        else:
            pusher.send_pyobj((func, args, kwargs))

    setattr(func, 'async', _async)

    return func
