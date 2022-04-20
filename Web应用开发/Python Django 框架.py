# -*- coding: UTF-8 -*-
if __name__ == '__main__':

    # TODO(You): 请在此添加创建django项目和初始化目录的命令
    create_django = 'django-admin startproject projectName'
    init_django = 'python manage.py startapp projectApp'

    installs = [
        "安装：pip install django",
        f"创建django项目命令：{create_django}",
        "进入目录：cd projectName",
        f"初始化django项目命令：{init_django}",
        "进一步查看教程：https://docs.djangoproject.com/zh-hans/3.2/"
    ]
    for step in installs:
        print(step)