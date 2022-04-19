# -*- coding: UTF-8 -*-
import os

def select(config):
    # 交互式选择程序，请理解这部分逻辑
    print(config['options_tip'])
    options = config['options']

    selects = []
    for key in options:
        desc = options[key]["desc"]
        selects.append(key)
        print(f"* {key}: {desc}")
    print()

    input_tip = config['input_tip']
    select_tip = '/'.join(selects)
    tip = f'{input_tip}[{select_tip}, 按q退出]：'

    while True:
        key = input(tip)
        if key == 'q':
            break

        option = options.get(key)
        if option:
            desc = option['desc']
            print(f"@{desc}:")
            option['action']()
        else:
            print("[错误] 不支持的选项")

def dump(tip, value):
    # 打印提示
    print(tip+':')
    print(value)
    print()

def dump_basic_info():
    # 打印基础信息
    dump('os.name', os.name)

def dump_path_info():
    # 打印路径信息
    dump('os.getcwd()', os.getcwd())
    dump('os.get_exec_path()', os.get_exec_path())

def dump_env_info():
    # 打印环境信息
    dump('os.environ', os.environ)

if __name__ == '__main__':
    select({
        # TODO(You): 请正确配置 select 的参数
        'options_tip': '通过 platform 可以查询一些有意思的信息',
        'input_tip': '请输入你感兴趣的信息',
        'options': {
            'b': {
                "desc": "b is basic, 系统基本信息",
                "action": dump_basic_info
            },
            'p': {
                "desc": "p is path, 路径信息",
                "action": dump_path_info
            },
            'e': {
                "desc": "e is env, 环境信息",
                "action": dump_env_info
            }
        },
    })