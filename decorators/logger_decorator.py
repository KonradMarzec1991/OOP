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
