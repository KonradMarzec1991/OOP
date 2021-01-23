def logger(fn):
    def wrapper(*args, **kwargs):
        print(f'Log: {fn.__name__}')
        return fn(*args, **kwargs)
    return wrapper


class MetaLogger(type):
    def __new__(mcls, *args, **kwargs):
        cls = super().__new__(mcls, *args, **kwargs)
        for name, obj in cls.__dict__.items():
            if callable(obj):
                print('Decorating callable', cls, name)
                setattr(cls, name, logger(obj))
        return cls


class Person(metaclass=MetaLogger):
    def __init__(self, name):
        self.name = name

    def hello(self):
        return f'{self.name} says hello!'
