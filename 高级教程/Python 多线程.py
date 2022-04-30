import threading
import time


def map_process(n):
    time.sleep(n)
    print(n)


def test():
    numbers = range(0, 3)
    for n in numbers:
        x = threading.Thread(target=map_process, args=(n,))
        x.start()


if __name__ == '__main__':
    test()