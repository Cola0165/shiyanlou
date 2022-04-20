# -*- coding: UTF-8 -*-
from error_code import ErrorCode
from jsonschema import validate
import json
import logging
import traceback
logger = logging.getLogger(__name__)

class KeyValueValidator:
    def __init__(self) -> None:
        pass

    def validate(self, req, required):
        '''使用jsonschema校验参数
        req: 请求参数
        required： 必须要有的字段
        '''
        # TODO(You): 请正确配置 jsonschema
        schema = {
            "type": "object",
            "properties": {
                "key": {"type": "string"},
                "value": {"type": "number"},
                "condition": {"type": "number"},
            },
            "required": required
        }

        try:
            validate(instance=req, schema=schema)
            return {
                'err': ErrorCode.SUCCESS
            }
        except Exception as e:
            logger.error(f"validate exception:{str(e)}")
            logger.error(traceback.format_exc())
            return {
                'err': ErrorCode.INVALID_PARAMETERS
            }


if __name__ == '__main__':
    v = KeyValueValidator()

    ret = v.validate({'key': "test", 'value': 100}, ['key', 'value'])
    assert ret['err'] == ErrorCode.SUCCESS
    ret = v.validate({'key': "test"}, ['key', 'value'])
    assert ret['err'] == ErrorCode.INVALID_PARAMETERS