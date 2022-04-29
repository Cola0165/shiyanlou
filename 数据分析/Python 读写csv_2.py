import os
import json
import csv
import logging
from enum import Enum


class ErrorCode(Enum):
    # 基本错误码
    SUCCESS = 0
    FAILED = 1
    NOT_FOUND = 2
    ALREADY_EXIST = 3

    # 数据库
    DB_OPEN_FAILED = 100
    DB_NOT_OPEN = 101
    DB_QUERY_EXCEPT = 102


logger = logging.Logger(__name__)


class CSVTable():
    def __init__(self, db_file, fieldnames) -> None:
        self.db_file = db_file
        self.fieldnames = fieldnames
        self.has_open = False

    def open(self):
        try:
            if self.has_open:
                return {"err": ErrorCode.SUCCESS}
            if not os.path.exists(self.db_file):
                with open(self.db_file, 'w', newline='') as csvfile:
                    writer = csv.DictWriter(
                        csvfile, fieldnames=self.fieldnames)
                    writer.writeheader()
            self.has_open = True
            return {"err": ErrorCode.SUCCESS}
        except Exception as e:
            logger.error('open redis exception:', str(e))
            self.conn = None
            return {"err": ErrorCode.DB_OPEN_FAILED}

    def close(self):
        return {'err': ErrorCode.SUCCESS}

    def append(self, row):
        if not self.has_open:
            return {"err": ErrorCode.DB_NOT_OPEN}

        assert type(row) == type({})

        try:
            with open(self.db_file, 'a', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=self.fieldnames)
                writer.writerow(row)
            return {'err': ErrorCode.SUCCESS}
        except Exception as e:
            logger.error(f'append exception:{str(e)}')
            return {"err": ErrorCode.DB_QUERY_EXCEPT}

    def select(self, filter):
        if not self.has_open:
            return {"err": ErrorCode.DB_NOT_OPEN}
        try:
            with open(self.db_file, newline='') as csvfile:
                reader = csv.DictReader(csvfile, fieldnames=self.fieldnames)
                results = []
                for row in reader:
                    if filter(row):
                        results.append(row)

            return {"err": ErrorCode.SUCCESS, "results": results}
        except Exception as e:
            logger.error(f'select exception:{str(e)}')
            return {"err": ErrorCode.DB_QUERY_EXCEPT}


if __name__ == "__main__":
    table = CSVTable('/tmp/csv_table.csv', ['name', 'age'])
    ret = table.open()
    assert ret['err'] == ErrorCode.SUCCESS

    table.append({"name": "Alice", "age": 18})
    table.append({"name": "Bob", "age": 18})

    ret = table.select(lambda item: item['age'] == '18')
    assert ret['err'] == ErrorCode.SUCCESS

    table.close()

    print(ret['results'])