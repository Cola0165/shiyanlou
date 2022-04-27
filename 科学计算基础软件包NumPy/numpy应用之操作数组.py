import numpy as np


def operate_array(operate, x, y):
    if operate == '+':
        print('数组相加：')
        res = x + y
        print(res)
        print('数组相加：numpy方法：')
        res = np.add(x, y)
        print(res)
    elif operate == '-':
        print('数组相减:')
        res = x - y
        print(res)
        print('数组相减，numpy方法：')
        res = np.subtract(x, y)
        print(res)
    elif operate == '*':
        print('数组相乘，逐元素矩阵乘法：')
        res = x * y
        print(res)
        print('数组相乘，numpy方法：逐元素矩阵乘法：')
        res = np.multiply(x, y)
        print(res)
    elif operate == '/':
        print('数组相除，对应元素相除：')
        res = x / y
        print(res)
        print('数组相除，numpy方法：对应元素相除：')
        res = np.divide(x, y)
        print(res)


if __name__ == '__main__':
    x = np.array([[1, 2, 3], [4, 5, 6]])
    y = np.array([[4, 5, 6], [7, 8, 9]])

    operate_array('+', x, y)
    operate_array('-', x, y)
    operate_array('*', x, y)
    operate_array('/', x, y)