def quantity(storage_name):

    def qty_getter(instance):
        return instance.__dict__.get(storage_name, None)

    def qty_setter(instance, value):
        if value > 0:
            instance.__dict__[storage_name] = value
        else:
            raise ValueError(f'{storage_name} must be greater than 0')

    return property(fget=qty_getter, fset=qty_setter)


class LineItem:
    weight = quantity('weight')
    price = quantity('price')

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price
