import threading


class Singleton(type):
    __singleton_lock = threading.Lock()
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            with Singleton.__singleton_lock:
                if cls not in cls._instances:
                    instance = super().__call__(*args, **kwargs)
                    cls._instances[cls] = instance
                    print("创建")

        print("返回")
        return cls._instances[cls]


class SingleClient(metaclass=Singleton):
    def __init__(self) -> None:
        pass


if __name__ == "__main__":
    s = SingleClient()
    s = SingleClient()
    s = SingleClient()