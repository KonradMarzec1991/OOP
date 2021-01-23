import inspect
import logging
from functools import wraps
from types import MethodType


def logger(fn):

    @wraps(fn)
    def wrapper(*args, **kwargs):
        print(f'Log: {fn.__name__} called')
        return fn(*args, **kwargs)
    return wrapper


class Logger:
    def __init__(self, fn):
        self.fn = fn

    def __call__(self, *args, **kwargs):
        print(f'Log: {self.fn.__name__} called')
        return self.fn(*args, **kwargs)

    def __get__(self, instance, owner):
        if instance is None:
            print('Returning self unbound...')
            return self
        else:
            print('Returning self as bound method to instance')
            return MethodType(self, instance)


class Person:
    def __init__(self, name):
        self.name = name

    @Logger
    def say_hello(self):
        return f'{self.name} says hello!'


def logged(level, name=None, message=None):
    """
    Add logging to a function, level is the
    logging level, name is the logger, and message
    is the log message. If name and message aren't
    specified, they default to the function's module and name.
    """

    def decorator(func):
        log_name = name if name else func.__module__
        log = logging.getLogger(log_name)
        log_msg = message if message else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, log_msg)
            return func(*args, **kwargs)
        return wrapper
    return decorator


def optional_debug(func):
    if 'debug' in inspect.getargspec(func).args:
        raise TypeError('debug argument already defined')

    @wraps(func)
    def wrapper(*args, debug=False, **kwargs):
        if debug:
            print('Calling', func.__name__)
        return func(*args, **kwargs)

    sig = inspect.signature(func)
    parms = list(sig.parameters.values())
    parms.append(inspect.Parameter(
        'debug',
        inspect.Parameter.KEYWORD_ONLY,
        default=False
    ))
    wrapper.__signature__ = sig.replace(parameters=parms)
    return wrapper
