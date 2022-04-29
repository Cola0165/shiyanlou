import os
import pandas as pd


class EasyExcelWriter:
    def __init__(self, excel_file) -> None:
        self.excel_file = excel_file

    def append_sheet(self, sheet_name, df):
        if not os.path.exists(self.excel_file):
            df.to_excel(self.excel_file, sheet_name=sheet_name)
        else:
            with pd.ExcelWriter(self.excel_file, mode='a') as writer:
                df.to_excel(writer, sheet_name=sheet_name)


class EasyExcelReader:
    def __init__(self, excel_file) -> None:
        self.excel_file = excel_file

    def load_sheet(self, sheet_name):
        return pd.read_excel(excel_file, sheet_name=sheet_name)


if __name__ == '__main__':

    df1 = pd.DataFrame(
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        index=['Alice', 'Bob', 'Middle'],
        columns=['a', 'b', 'c']
    )

    df2 = pd.DataFrame([["AAA", "BBB"]], columns=["Spam", "Egg"])
    df3 = pd.DataFrame([["ABC", "XYZ"]], columns=["Foo", "Bar"])

    excel_file = '/tmp/panda_excel.xlsx'

    w = EasyExcelWriter(excel_file)
    w.append_sheet('table1', df1)
    w.append_sheet('table2', df2)
    w.append_sheet('table3', df3)

    r = EasyExcelReader(excel_file)
    df = r.load_sheet('table2')
    print(df.head())