import pandas as pd
import numpy as np

# 该函数的输出数据只含有 cloumn_one  cloumn_two  cloumn_three 三个列
def create_dataframe_from_list():
    # TODO(You)：请在此编写代码
    data = {
        'cloumn_one': np.random.randint(0, 10, size=5),
        'cloumn_two': np.random.randint(0, 10, size=5),
        'cloumn_three': np.random.randint(0, 10, size=5)
    }
    data_df = pd.DataFrame(data)
    return data_df

# 该函数的输出数据只含有 cloumn_one  cloumn_two  cloumn_three 三个列
def create_dataframe_from_series():
    # TODO(You)：请在此编写代码
    data = {
    'cloumn_one': pd.Series(np.random.randint(0, 10, size=5)),
    'cloumn_two': pd.Series(np.random.randint(0, 10, size=5)),
    'cloumn_three': pd.Series(np.random.randint(0, 10, size=5))
}
    data_df = pd.DataFrame(data)
    return data_df

# 该函数的输出数据只含有 cloumn_one  cloumn_two  cloumn_three 三个列
def create_dataframe_from_2darray():
    # TODO(You)：请在此编写代码
    data = [
        [3, 5, 2],
        [2, 7, 9],
        [5, 6, 9]
    ]
    data_df = pd.DataFrame(
        data, columns=['cloumn_one', 'cloumn_two', 'cloumn_three'])
    return data_df

# 该函数的输出数据只含有 cloumn_one  cloumn_two  cloumn_three 三个列
def create_dataframe_from_dict():
   # TODO(You)：请在此编写代码
    data = [{'cloumn_one': 1, 'cloumn_two': 2, 'cloumn_three': 3},
            {'cloumn_one': 5, 'cloumn_two': 6, 'cloumn_xxx': 7}]
    data_df = pd.DataFrame(data)
    return data_df


if __name__ == '__main__':
    print('由数组list组成的字典创建dataframe:')
    data_df = create_dataframe_from_list()
    print(data_df)

    print('由Series组成的字典创建dataframe:')
    data_df = create_dataframe_from_series()
    print(data_df)

    print('通过二维数组直接创建dataframe:')
    data_df = create_dataframe_from_2darray()
    print(data_df)

    print('由字典组成的列表创建dataframe:')
    data_df = create_dataframe_from_dict()
    print(data_df)