def test():
    sci_py_meta = {
        "title": "Scientific computing tools for Python",
        "title_zh_cn": "Python 科学计算软件包",
        "sub_title": 'SciPy refers to several related but distinct entities:',
        "sub_title_zh_cn": 'SciPy 指向一组相关但互相独立的软件包',
        "desc": [
            'The SciPy ecosystem, a collection of open source software for scientific computing in Python.',
            'The community of people who use and develop this stack.',
            'Several conferences dedicated to scientific computing in Python - SciPy, EuroSciPy, and SciPy.in.',
            'The SciPy library, one component of the SciPy stack, providing many numerical routines.',
        ],
        "desc_zh_ch": [
            'SciPy 本身也是一个Python库, 属于 SciPy 技术栈的一员, 提供了许多数值计算程序.',
            '许多 Python 相关的科学计算会议，例如  SciPy, EuroSciPy, 和 SciPy 等',
            '使用和开发这组技术栈的人',
            'SciPy 生态是指一组开源 Python 科学计算软件',
        ],
        "packages": [
            "Python", "NumPy", "SciPy library", "Matplotlib", "pandas", "SymPy", "NetworkX", "scikit-image",
            "scikit-learn", "h5py", "PyTables", "IPython", "Jupyter", "Cython", "Dask", "Joblib", "IPyParallel",
            "nose", "numpydoc"
        ]
    }

    print()
    print("# {}".format(sci_py_meta['title_zh_cn']))
    print("# {}".format(sci_py_meta['title']))
    print()

    print("* {}".format(sci_py_meta['sub_title_zh_cn']))
    print("* {}".format(sci_py_meta['sub_title']))
    print()

    print("* 描述:")
    for i in range(0, len(sci_py_meta['desc'])):
        print("  * {}".format(sci_py_meta['desc_zh_ch'][i]))
        print("  * {}".format(sci_py_meta['desc'][i]))
        print()

    print("* 相关Python 软件栈：")
    for pkg in sci_py_meta['packages']:
        print("  * {}".format(pkg))


if __name__ == '__main__':
    test()