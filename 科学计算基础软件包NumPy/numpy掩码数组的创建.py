import numpy as np


def create_mask_array(array_a, mask_list):
    mask = np.zeros(len(array_a), dtype=int)
    for i in mask_list:
        mask[i] = 1

    y = np.ma.array(array_a, mask=mask)
    return y


if __name__ == '__main__':
    a = np.random.randint(0, 10, size=(10))
    b = create_mask_array(a, [0, 1, 2, 3, 4])
    assert np.mean(b) == np.mean(a[5:])