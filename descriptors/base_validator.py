import numbers


class BaseValidator:
    def __init__(self, min_=None, max_=None):
        self._min = min_
        self._max = max_

    def __set_name__(self, owner, name):
        self.property_name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.property_name, None)

    def validate(self, value):
        # this will need to be implemented specifically for each subclass
        pass

    def __set__(self, instance, value):
        self.validate(value)
        instance.__dict__[self.property_name] = value


class IntegerField(BaseValidator):

    def validate(self, value):
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


class CharField(BaseValidator):
    def __init__(self, min_, max_):
        min_ = max(min_ or 0, 0)
        super().__init__(min_, max_)

    def validate(self, value):
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
