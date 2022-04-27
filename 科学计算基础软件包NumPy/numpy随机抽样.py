import numpy as np


def random_sample(array, num):
    if num <= len(array):
        return np.random.choice(array, num)
    else:
        return None


if __name__ == '__main__':
    a = [i for i in range(10)]
    print('输入的数据：{}'.format(a))

    ret = random_sample(a, 11)
    assert ret is None
    print('随机抽样个数不能超过原始数组大小')

    ret = random_sample(a, 2)
    assert len(ret) == 2
    print('随机抽样结果：{}'.format(ret))