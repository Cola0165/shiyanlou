# -*- coding: UTF-8 -*-
import logging
import json
from error_code import ErrorCode
from redis_connector import RedisConnector
logger = logging.Logger(__name__)
redis_connection = None
        
class RedisKeyValueStore(RedisConnector):
    def __init__(self, host, port, password) -> None:
        super().__init__(host, port, password)

    def set(self, key, value):
        # TODO(You): 请在此实现Redis写入代码
        if self.conn is None:
            return {'err': ErrorCode.DB_OPEN_FAILED}

        try:
            self.conn.set(key, json.dumps(value))
            return {'err': ErrorCode.SUCCESS}
        except Exception as e:
            logger.error(f'set key:{key} exception:{str(e)}')
            return {"err": ErrorCode.DB_QUERY_EXCEPT}

    def get(self, key):
        if self.conn is None:
            return {'err': ErrorCode.DB_NOT_OPEN}

        try:
            results = self.conn.get(key)
            if results is None:
                return {"err": ErrorCode.NOT_FOUND}
            return {"err": ErrorCode.SUCCESS, "key": key, "value": json.loads(results)}
        except Exception as e:
            logger.error(f'get key:{key} exception:{str(e)}')
            return {"err": ErrorCode.DB_QUERY_EXCEPT}


if __name__ == '__main__':
    kv = RedisKeyValueStore("127.0.0.1", 6379, None)
    ret = kv.open()
    assert ret['err'] == ErrorCode.SUCCESS

    ret = kv.set("test", {"number": 0})
    assert ret['err'] == ErrorCode.SUCCESS

    ret = kv.get("test")
    assert ret['err'] == ErrorCode.SUCCESS
    assert ret['value']['number'] == 0

    ret = kv.close()
    assert ret['err'] == ErrorCode.SUCCESS