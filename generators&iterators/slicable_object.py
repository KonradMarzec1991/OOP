import numbers


class Vector:
    def __init__(self, components):
        self._components = components

    def __getitem__(self, key):
        if isinstance(key, slice):
            pass
        elif isinstance(key, numbers.Integral):
            pass
        else:
            pass
