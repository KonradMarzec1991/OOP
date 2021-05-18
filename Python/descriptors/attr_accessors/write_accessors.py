class NonDataDescriptor:
    def __get__(self, instance, owner):
        print('__get__ called from non data descriptor')


class DataDescriptor:
    def __set__(self, instance, value):
        print('__set__ called from data descriptor')

    def __get__(self, instance, owner):
        print('__get__ called from data descriptor')


class MyClass:
    non_data_desc = NonDataDescriptor()
    data_desc = DataDescriptor()

    def __setattr__(self, key, value):
        print('__setattr__ called')
        super().__setattr__(key, value)