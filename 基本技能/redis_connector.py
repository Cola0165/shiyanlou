# -*- coding: UTF-8 -*-
import logging
import json
from error_code import ErrorCode
import redis
logger = logging.Logger(__name__)

redis_connection_pool = None   
class RedisConnector():
    def __init__(self, host, port, password) -> None:
        global redis_connection_pool
        if redis_connection_pool is None:
            redis_connection_pool = redis.ConnectionPool(
                host=host,
                port=port,
                password=password
            )
        self.conn = None

    def open(self):
        # TODO(You): 请在此实现打开 redis 代码
        if self.conn is not None:
            return {"err": ErrorCode.SUCCESS}

        try:
            self.conn = redis.StrictRedis(
                connection_pool=redis_connection_pool)
            return {"err": ErrorCode.SUCCESS}
        except Exception as e:
            logger.error('open redis exception:', str(e))
            self.conn = None
            return {"err": ErrorCode.DB_OPEN_FAILED}

    def close(self):
        if self.conn is not None:
            self.conn.close()
            self.conn = None
        return {'err': ErrorCode.SUCCESS}

if __name__ == '__main__':
    redis_connector = RedisConnector("127.0.0.1", 6379, None)

    ret = redis_connector.open()
    assert ret['err'] == ErrorCode.SUCCESS
    ret = redis_connector.close()
    assert ret['err'] == ErrorCode.SUCCESS