import abc


class AutoStorage:
    __counter = 0

    def __init__(self):
        cls = self.__class__
        prefix = cls.__name__
        index = self.__counter
        self.storage_name = f'_{prefix}#{index}'
        self.__counter += 1

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            return getattr(instance, self.storage_name, None)

    def __set__(self, instance, value):
        setattr(instance, self.storage_name, value)


class Validated(abc.ABC, AutoStorage):

    def __set__(self, instance, value):
        value = self.validate(instance, value)
        super().__set__(instance, value)

    @abc.abstractmethod
    def validate(self, instance, value):
        """Returns validated value or raise ValueError"""


class Quantity(Validated):
    def validate(self, instance, value):
        if isinstance(value, int) and value > 0:
            return value
        else:
            raise ValueError(f'{value} must be a positive int type')


class NonBlank(Validated):
    def validate(self, instance, value):
        value = value.strip()
        if isinstance(value, str) and len(value) > 0:
            return value
        else:
            raise ValueError(f'{value} must be string with len > 0')


class LineItem:
    description = NonBlank()
    weight = Quantity()
    price = Quantity()

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price
