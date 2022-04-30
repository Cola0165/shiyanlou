def test():
    list = [1, 2, 3, 4, 5, 6]
    for v in map(lambda v: v*v, list):
        print(v)


if __name__ == '__main__':
    test()