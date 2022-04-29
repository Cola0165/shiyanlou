import os
import json


def load_json(file):
    if not os.path.exists(file):
        return None
    with open(file, 'r') as f:
        return json.loads(f.read())


def dump_json(file, obj):
    with open(file, 'w') as f:
        f.write(json.dumps(obj, indent=2, ensure_ascii=False))


def pip_install(pkg):
    try:
        ret = os.system(f'pip install {pkg}')
        return {"err": 0, "msg": f"install {pkg} success, info:{ret}"}
    except Exception as e:
        return {"err": 1, "msg": f"install {pkg} exception: {str(e)}"}


def pip_install_list(name, packages):
    save_point_file = f"/tmp/pip_install_{name}.json"
    save_point = load_json(save_point_file)
    index = save_point['index'] if save_point else 0
    while index < len(packages):
        ret = pip_install(packages[index])
        print(ret['msg'])

        if ret['err'] != 0:
            break

        dump_json(save_point_file, {"index": index})
        index += 1


if __name__ == "__main__":
    packages = [
        "numpy", "scipy", "matplotlib", "ipython", "jupyter", "pandas", "sympy", "nose"
    ]
    pip_install_list("[scipy]", packages)