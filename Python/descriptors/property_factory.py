import numbers


# property factory
def quantity(storage_name):

    def qty_getter(instance):
        return instance.__dict__.get(storage_name, None)

    def qty_setter(instance, value):
        if value > 0:
            instance.__dict__[storage_name] = value
        else:
            raise ValueError(f'{storage_name} must be greater than 0')

    return property(fget=qty_getter, fset=qty_setter)


# descriptor
class Quantity:
    def __init__(self, storage_name):
        self.storage_name = storage_name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.storage_name, None)

    def __set__(self, instance, value):
        if not isinstance(value, numbers.Integral):
            raise ValueError(f'{self.storage_name} must be integral number')
        if value <= 0:
            raise ValueError(f'{self.storage_name} must be greater than 0')
        instance.__dict__[self.storage_name] = value


# descriptor with no storage_name
class QualityDescriptor:
    __counter = 0

    def __init__(self):
        cls = self.__class__
        prefix = cls.__name__
        index = cls.__counter
        self.storage_name = f'_{prefix}#{index}'
        cls.__counter += 1

    def __get__(self, instance, owner):
        return getattr(instance, self.storage_name, None)

    def __set__(self, instance, value):
        if not isinstance(value, numbers.Integral):
            raise ValueError(f'{self.storage_name} must be integral number')
        if value <= 0:
            raise ValueError(f'{self.storage_name} must be greater than 0')
        setattr(instance, self.storage_name, value)


class LineItem:
    weight = QualityDescriptor()
    price = QualityDescriptor()

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price
