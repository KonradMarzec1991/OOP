from descriptors.auto_storage import (
    NonBlank,
    Quantity,
    Validated
)


# basic decorator
def entity(cls):
    for key, attr in cls.__dict__.items():
        if isinstance(attr, Validated):
            type_name = type(attr).__name__
            attr.storage_name = f'{type_name}#{key}'
    return cls


# metaclass
class EntityMeta(type):
    def __new__(mcls, class_name, class_bases, class_dict):
        cls = super().__new__(mcls, class_name, class_bases, class_dict)
        cls._fields_names = []
        for key, attr in cls.__dict__.items():
            if isinstance(attr, Validated):
                type_name = type(attr).__name__
                attr.storage_name = f'{type_name}#{key}'
                cls._fields_names.append(key)
        return cls


# main class
class Entity(metaclass=EntityMeta):
    pass


class LineItem(Entity):
    description = NonBlank()
    weight = Quantity()
    price = Quantity()

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price

    @classmethod
    def fields_names(cls):
        for key in cls._fields_names:
            yield key


for name in LineItem.fields_names():
    print(name)


