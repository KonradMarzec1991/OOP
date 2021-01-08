class SingletonTry:
    _existing_instance = None

    def __new__(cls):
        if not cls._existing_instance:
            print('creating new instance...')
            new_instance = super().__new__(cls)
            setattr(new_instance, 'name', 'hundred')
            setattr(new_instance, 'value', 100)
            cls._existing_instance = new_instance
        else:
            print('instance exists already, using that one...')
        return cls._existing_instance


class Singleton(type):
    instances = {}

    def __call__(cls, *args, **kwargs):
        print(f'Request received to create an instance of class: {cls.__name__}')
        existing_instance = Singleton.instances.get(cls, None)
        if existing_instance is None:
            Singleton.instances[cls] = super().__call__(*args, **kwargs)
        return Singleton.instances[cls]
