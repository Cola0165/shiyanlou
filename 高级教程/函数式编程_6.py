def dispatch(actions, targets):
    action_len = len(actions)
    index = 0
    next = targets
    action = actions[index]

    while action_len >= index:
        if type(next) == type({}):
            if index == action_len:
                if next.get('run') != None:
                    next['run']()
                    break

            action = actions[index]
            if next.get(action) != None:
                next = next[action]
                index += 1
            else:
                index += 1
        else:
            next()
            index += 1
            break


def route(input):
    # 路由器在路由到的节点上执行命令
    dispatch(input.split('.'), {
        "a": {
            "run": lambda: print("A"),
            "b": {
                "run": lambda: print("A.B"),
                "c": {
                    "run": lambda: print("A.B.C"),
                    "d": lambda: print("A.B.C.D"),
                }
            }
        }
    })


if __name__ == "__main__":
    route("a")
    route("a.b")
    route("a.b.c")
    route("a.b.c.d")