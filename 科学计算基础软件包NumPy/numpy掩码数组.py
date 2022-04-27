import numpy as np


def test():
    x = np.array([1, 2, 3, -1, 5])
    y = np.ma.masked_array(x, mask=[0, 0, 0, 1, 0])
    print('查看y的值: ')
    for idx, val in enumerate(y):
        print('y[{}] = {}'.format(idx, val))

    assert type(y[3]) is np.ma.core.MaskedConstant

    print('y的平均值: {}'.format(np.mean(y)))
    assert np.mean(y) == 2.75


if __name__ == '__main__':
    test()