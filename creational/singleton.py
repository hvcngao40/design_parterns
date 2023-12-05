'''Nếu bạn muốn 1 class chỉ có duy nhất 1 instance (ví dụ như kết nối database, file) thì singleton chính là lựa chọn'''

class Singleton:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

#################################


def singleton(cls):
    instance = None
    def wrapper(*args, **kwargs):
        nonlocal instance
        if not instance:
            instance = cls(*args, **kwargs)
        return instance

    return wrapper

@singleton
class SingletonByDecorator:
    pass

###################################

@singleton
class Singleton2:
    _instance = None

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if not cls._instance:
            instance = super().__call__(*args, **kwargs)
            cls._instance = instance
        return cls._instance



if __name__ == '__main__':
    obj1 = Singleton()
    obj2 = Singleton()
    print(obj1 is obj2)

    obj1 = SingletonByDecorator()
    obj2 = SingletonByDecorator()
    print(obj1 is obj2)

    obj1 = Singleton2()
    obj2 = Singleton2()
    print(obj1 is obj2)
