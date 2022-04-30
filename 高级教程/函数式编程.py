def test():
    list = [1, 2, 3, 4, 5, 6]
    for v in filter(lambda v: v % 2 == 0, list):
        print(v)


if __name__ == '__main__':
    test()