# -*- coding: UTF-8 -*-
import platform

def select(config, show_info):
    print(config['options_tip'])

    selects = []
    for key in config['options']:
        option = config['options'][key]
        selects.append(key)
        print(f"* {key}: {option}")

    tip = f"{config['input_tip']}[{'/'.join(selects)}, 按q退出]："
    while True:
        key = input(tip)
        if key == 'q':
            break
        else:
            show_info(key)
            print()

def test():
    def show_info(key):
        if key == 'p':
            # TODO(You): 打印平台信息
            print(platform.architecture())
            print(platform.platform())
            print(platform.processor())
            print(platform.machine())
        elif key == 'py':
            # TODO(You): 打印Python信息
            print(platform.python_build())
            print(platform.python_implementation())
            print(platform.python_compiler())
            print(platform.python_version())

    select({
        'options_tip': '通过 platform 可以查询一些有意思的信息',
        'input_tip': '请输入你感兴趣的信息',
        'options': {
            'p': "p is platform, 平台信息",
            'py': "py is python, Python 信息",
        },
    }, show_info)

if __name__ == '__main__':
    test()