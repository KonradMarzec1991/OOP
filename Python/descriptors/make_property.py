class MakeProperty:
    def __init__(self, fget=None, fset=None):
        self.fget = fget
        self.fset = fset

    def __set_name__(self, owner, name):
        self.property_name = name

    def __get__(self, instance, owner):
        print('__get__ called')
        if instance is None:
            return self
        if self.fget is None:
            raise AttributeError(f'{self.fget} is not readable.')
        return self.fget(instance)

    def __set__(self, instance, value):
        print('__set__ called')
        if self.fset is None:
            raise AttributeError(f'{self.fset} is not writable.')
        self.fset(instance, value)

    def setter(self, fset):
        self.fset = fset
        return self


class Person:

    @MakeProperty
    def age(self):
        return getattr(self, '_age', None)

    @age.setter
    def age(self, value):
        self._age = value
