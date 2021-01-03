from functools import wraps


def account_type(type_):
    def inner(cls):
        cls.account_type = type_
        return cls
    return inner


class Account:
    pass


@account_type('Savings')
class BankSavings(Account):
    pass


@account_type('Checking')
class BankChecking(Account):
    pass


def hello(cls):
    cls.hello = lambda self: f'{self} says hello!'
    return cls


@hello
class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


def class_logger(cls):

    def func_logger(fn):
        def inner(*args, **kwargs):
            result = fn(*args, **kwargs)
            print(f'Log: {fn.__qualname__} ({args}, {kwargs}) = {result}')
            return result

        return inner

    for name, obj in vars(cls).items():
        if callable(obj):
            print('decorating: ', cls, name)
            setattr(cls, name, func_logger(obj))
    return cls


@class_logger
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def great(self):
        return f'Hello my name is {self.name}, and I am {self.age} years old'
