class Singleton:
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


