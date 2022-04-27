import numpy as np


if __name__ == '__main__':
    print('创建一维数组')
    print(np.array([1, 2, 3, 4]))

    print('创建二维数组')
    print(np.array([[1, 2], [3, 4]]))

    print("创建三维数组")
    print(np.array([[[1, 2], [3, 4]],
                    [[5, 6], [7, 8]]]))

    print("转换类型")
    b = np.array([-1, 0, 7], dtype=np.int32)
    assert (b.astype(np.bool_) == [True, False, True]).all()