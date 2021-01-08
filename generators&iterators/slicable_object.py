from array import array
import reprlib
import numbers


class Vector:
    type_code = 'd'

    def __init__(self, components):
        self._components = array(self.type_code, components)

    def __getitem__(self, key):
        cls = type(self)
        if isinstance(key, slice):
            return cls(self._components[key])
        elif isinstance(key, numbers.Integral):
            return self._components[key]
        else:
            msg = '{cls.__name__} indices must be integers'
            raise TypeError(msg.format(cls=cls))

    def __len__(self):
        return len(self._components)

    def __repr__(self):
        components = reprlib.repr(self._components)
        components = components[components.find('['):-1]
        return 'Vector({})'.format(components)