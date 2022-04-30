from functools import reduce


def my_reduce(accumulate, list, init):
    total = init
    for e in list:
        total = accumulate(total, e)
    return total


if __name__ == '__main__':
    list = [1, 2, 3, 4, 5, 6]

    sum = reduce(lambda x, y: x+y, list)
    print(sum)

    prod = reduce(lambda x, y: x*y, list)
    print(prod)

    print(my_reduce(lambda x, y: x+y, list, 0))
    print(my_reduce(lambda x, y: x*y, list, 1))