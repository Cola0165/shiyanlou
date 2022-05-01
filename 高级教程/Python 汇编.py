import dis

if __name__ == "__main__":
    code_str = """
print("Hello,world!")
print("Hello,world!")
"""
    code_obj = compile(code_str, '<string>', 'exec')

    ins = dis.get_instructions(code_obj)
    hello_world_il_count = 0
    for il in ins:
        if il.argval == 'Hello,world!':
            print(il)
            hello_world_il_count += 1
    assert hello_world_il_count == 2