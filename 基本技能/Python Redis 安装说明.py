# -*- coding: UTF-8 -*-
def dump_depends(depends):
    print()
    print("# 依赖配置")
    for i in range(0, len(depends)):
        print("{}. {}".format(i, depends[i]))

if __name__ == '__main__':
    start_server = 'redis-server'#TODO(You): 请编写启动 redis 服务命令
    login_redis = 'redis-cli -h 127.0.0.1 -p 6379'#TODO(You): 请编写登录到 redis 的命令 

    dump_depends([
        '安装 redis ：https://redis.io/download',
        f'启动 redis 服务： {start_server}',
        f'进入 redis 命令行客户端: {login_redis}',
        '库安装: pip install redis',
    ])