# -*- coding: UTF-8 -*-
def dump_depends(depends):
    print()
    print("# 依赖配置")
    for i in range(0, len(depends)):
        print("{}. {}".format(i, depends[i]))


if __name__ == '__main__':

    # TODO(You): 请编写 db 和 login_commands 两个变量
    db = '''
create database test;
use test;
create table if not exists key_value (
    _key varchar(32) not NULL,
    value  text not NULL,
    PRIMARY KEY (`_key`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;
'''
    login_commands = 'mysql -h 127.0.0.1 -P 3306 -u root -p'

    dump_depends([
        '安装 MySQL : https://dev.mysql.com/downloads/installer/'
        '启动 MySQL 本地服务: 每个平台不同',
        f'登录数据库：{login_commands}',
        f'请创建初始化数据库:\n{db}',
        'Python 库安装： pip install mysql-connector-python',
    ])