# 可以通过数组转为矩阵
# 矩阵 b :
# <code>
# [[3 9 4]
#  [6 7 9]
#  [3 5 7]]
# </code>

# b的转置矩阵为：
# <code>
# [[3 6 3]
#  [9 7 5]
#  [4 9 7]]
# </code>

# b的逆矩阵：
# <code>
# [[-0.04597701  0.49425287 -0.6091954 ]
#  [ 0.17241379 -0.10344828  0.03448276]
#  [-0.10344828 -0.13793103  0.37931034]]
# </code>

import numpy as np


if __name__ == '__main__':
    a = np.random.randint(0, 10, size=(3, 3))
    matrix_b = np.matrix(a)
    print(matrix_b)
    print(matrix_b.T)
    print(matrix_b.I)