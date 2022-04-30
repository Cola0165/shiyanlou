from functools import wraps


def auto_log(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f'函数:{func.__name__}, 参数:{str(args)}, 命名参数:{str(kwargs)}')
        return func(*args, **kwargs)
    return wrapper


class Test(object):

    def __init__(self):
        pass

    @auto_log
    def test(self, a, b, c, d, x=None):
        print("test")


if __name__ == '__main__':
    t = Test()
    c = t.test("你好", "世界", 1, 2, x="xxx")