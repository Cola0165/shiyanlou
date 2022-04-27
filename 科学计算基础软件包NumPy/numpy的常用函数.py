import numpy as np


if __name__ == '__main__':
    data = np.random.randint(0, 10, size=(10))
    print('输入数据: {}'.format(data))

    data_sum = np.sum(data)
    print('求和: {}'.format(data_sum))

    data_mean = np.mean(data)
    print('求平均: {}'.format(data_mean))

    data_std = np.std(data)
    print('求标准差: {}'.format(data_std))

    data_var = np.var(data)
    print('求方差: {}'.format(data_var))

    data_min = np.min(data)
    print('求最小值: {}'.format(data_min))

    data_max = np.max(data)
    print('求最大值: {}'.format(data_max))

    data_median = np.median(data)
    print('求中位数: {}'.format(data_median))

    data_unique = np.unique(data)
    print('找出数组中所有不同的值，并按从小打大排序： {}'.format(data_unique))