class PersonClass:
    def __init__(self, age):
        self._age = age

    def __getattr__(self, name):
        alt_name = '_' + name
        print(f'Could not find {name}, trying {alt_name}')

        try:
            return super().__getattribute__(alt_name)
        except AttributeError:
            raise AttributeError(f'Could not find {name} or {alt_name}')


class AttributeNotFoundLogger:
    def __getattr__(self, name):
        err_msg = f'{type(self).__name__} object has no attribute {name}'
        print(f'Log: {err_msg}')
        raise AttributeError(err_msg)


class DefaultClass:
    def __init__(self, attr_default=None):
        self._attr_default = attr_default

    def __getattr__(self, name):
        print(f'{name} not found, creating and setting it to default')
        default_value = super().__getattribute__('_attr_default')
        setattr(self, name, default_value)
        return default_value


class Person(DefaultClass):
    def __init__(self, name, age):
        super().__init__('Not Available')
        if name is not None:
            self._name = name
        if name is not None:
            self._age = age

    def __getattribute__(self, name):
        if name.startswith('_') and not name.startswith('__'):
            raise AttributeError(f'Forbidden access to {name}')
        return super().__getattribute__(name)

    @property
    def name(self):
        return super().__getattribute__('_name')

    @property
    def age(self):
        return super().__getattribute__('_age')