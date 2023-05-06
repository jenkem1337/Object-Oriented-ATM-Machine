

class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class SessionManager(metaclass=SingletonMeta):
    __keyValuePair = dict()

    def setKeyValuePair(self, k, v):
        if k is None:
            raise Exception("Anahtar sözcüğü boş olamaz")

        if v is None:
            raise Exception("Değer sözcüğü boş olamaz")
        self.__keyValuePair[k] = v
        return self

    def getValue(self, k):
        if k is None:
            raise Exception("Anahtar sözcüğü boş olamaz")

        return self.__keyValuePair.get(k)

    def clear(self):
        self.__keyValuePair.clear()
