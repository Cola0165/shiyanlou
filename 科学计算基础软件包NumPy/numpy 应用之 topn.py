import numpy as np


def get_top_n(array, top_n):
    top_n_indexs = np.argsort(array)[:-(top_n+1):-1]
    results = [array[index] for index in top_n_indexs]
    return results


if __name__ == '__main__':
    ret = get_top_n(np.array([1, 3, 34, 4, 5, 6]), 3)
    print(ret)