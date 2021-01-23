class AutoClassAttrib(type):
    def __new__(mcls, name, bases, cls_dict, **extra_attrs):
        print('Creating class with some extra attributes', extra_attrs)
        cls_dict.update(extra_attrs)
        cls = super().__new__(mcls, name, bases, cls_dict)
        return cls


class Account(metaclass=AutoClassAttrib, account_type='Savings', apr=0.5):
    pass


class MyMeta(type):
    def __new__(mcls, name, bases, cls_dict, **kwargs):
        cls_dict.update(kwargs)
        return super().__new__(mcls, name, bases, cls_dict)


class MyClass(metaclass=MyMeta, k1=1, k2=2):
    pass
