import numbers


class IntegerField:
    def __init__(self, min_, max_):
        self._min = min_
        self._max = max_

    def __set_name__(self, owner, name):
        self.property_name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.property_name, None)

    def __set__(self, instance, value):
        if not isinstance(value, numbers.Integral):
            raise ValueError(f'{self.property_name} must be an int')
        if value < self._min:
            raise ValueError(
                f'{self.property_name} must be greater than {self._min}'
            )
        if value > self._max:
            raise ValueError(
                f'{self.property_name} must be lower than {self._max}'
            )
        instance.__dict__[self.property_name] = value


class CharField:
    def __init__(self, min_=None, max_=None):
        min_ = 0 or min_
        min_ = max(0, min_)
        self._min = min_
        self._max = max_

    def __set_name__(self, owner, name):
        self.property_name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.property_name, None)

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError(f'{self.property_name} must be a string')
        if self._min is not None and len(value) < self._min:
            raise ValueError(
                f'{self.property_name} must be greater than {self._min} chars.'
            )
        if self._max is not None and len(value) > self._max:
            raise ValueError(
                f'{self.property_name} must be lower than {self._max} chars.'
            )
        instance.__dict__[self.property_name] = value
