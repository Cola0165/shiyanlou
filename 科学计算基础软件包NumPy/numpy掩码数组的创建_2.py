import numpy as np


def create_condition_mask_array(array_a, val):
    mask = np.zeros(len(array_a), dtype=int)
    for i in range(len(array_a)):
        if array_a[i] >= val:
            mask[i] = 1

    y = np.ma.array(array_a, mask=mask)
    return y


if __name__ == '__main__':
    a = np.random.randint(0, 10, size=(10))
    b = create_condition_mask_array(a, 5)

    na = [x for x in a if x < 5]
    nb = [x for x in b if type(x) is not np.ma.core.MaskedConstant]

    assert na == nb