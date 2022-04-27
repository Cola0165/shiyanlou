import numpy as np


if __name__ == '__main__':
    examples = np.array([
        [
            "创建单位矩阵",
            "创建对角矩阵",
            "创建范德蒙矩阵"
        ],
        [
            lambda: np.eye(3),
            lambda: np.diag([1, 2, 3]),
            lambda: np.vander(np.linspace(0, 2, 5), 2)
        ]
    ])

    for i in range(examples.shape[1]):
        tip = examples[0][i]
        action = examples[1][i]
        print(tip)
        print(action())