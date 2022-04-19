# -*- coding: UTF-8 -*-
from enum import Enum

class ErrorCode(Enum):
    # TODO(You): 请在此定义错误
    SUCCESS = 0
    FAILED = 1
    NOT_FOUND = 2
    ALREADY_EXIST = 3
    INVALID_PARAMETERS = 4

    @staticmethod
    def internal_ret_2_http(ret):
        ret['err'] = ret['err'].name.lower()

if __name__ == '__main__':
    ret = {'err': ErrorCode.NOT_FOUND}
    ErrorCode.internal_ret_2_http(ret)
    assert ret['err'] == 'not_found'