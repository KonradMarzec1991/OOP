class Point2D:
    _fields = ['x', 'y']

    def __init__(self, x, y):
        self._x = x
        self._y = y


class Point3D:
    _fields = ['x', 'y', 'z']

    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z


class SlottedStruct(type):
    def __new__(mcls, name, bases, cls_dict):
        cls_object = super().__new__(mcls, name, bases, cls_dict)

        # __slots__
        setattr(
            cls_object,
            '__slots__',
            [f'_{field}' for field in cls_object._fields]
        )

        # read-only properties
        for field in cls_object._fields:
            slot = f'_{field}'
            setattr(
                cls_object,
                field,
                property(fget=lambda self, attrib=slot: getattr(self, attrib))
            )

        return cls_object


class Person(metaclass=SlottedStruct):
    _fields = ['name', 'age']

    def __init__(self, name, age):
        self._name = name
        self._age = age
