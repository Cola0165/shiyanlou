import numpy as np

if __name__ == '__main__':
    shape = (3, 3)

    print('创建0数组，元素全部为0，用dtype参数指定数据类型')
    print(np.zeros(shape, dtype=int))

    print('创建元素全为1的数组，用dtype指定数据类型')
    print(np.ones(shape, dtype=int))

    print('创建范围序列，用dtype指定数据类型')
    print(np.arange(2, 10, dtype=float))

    print('创建未初始化的数组')
    print(np.empty(shape, dtype=int))