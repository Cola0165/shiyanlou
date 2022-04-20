# -*- coding: UTF-8 -*-
from error_code import ErrorCode
import json
import logging
import traceback
logger = logging.getLogger(__name__)

class Router:
    def __init__(self, routes) -> None:
        self.routes = routes

    def dispatch(self, http_request_str):
        # TODO(You)： 请实现路由逻辑，返回符合语义的HTTP状态码
        req_path = None
        req = None
        try:
            http_request = json.loads(http_request_str)
            req_path = http_request.get('path')
            req = http_request.get('data')
        except Exception as e:
            logger.error(f"parse data exception:{str(e)}")
            return {'err': ErrorCode.INVALID_PARAMETERS}, 400

        if req_path is None or self.routes.get(req_path) is None:
            return {'err': ErrorCode.NOT_FOUND}, 404

        try:
            handler = self.routes.get(req_path)
            return handler(req), 200
        except Exception as e:
            logger.error(f"route to '{req_path}' exception:{str(e)}")
            logger.error(traceback.format_exc())
            return {'err': ErrorCode.FAILED}, 500
            
if __name__ == '__main__':
    # 注册路由
    router = Router({
        '/': lambda req: print(f'goto home:{str(req)}')
    })

    # 分发路由
    router.dispatch(json.dumps({
        'path': '/',
        'data': ["Hello", "World!"]
    }))