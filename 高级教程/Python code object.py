if __name__ == "__main__":
    code_str = """
print("Hello,world!")
print("Hello,world!")
"""
    code_obj = compile(code_str, '<string>', 'exec')
    exec(code_obj)
    print(code_obj.co_name)
    print(code_obj.co_filename)
    print(code_obj.co_argcount)
    print(code_obj.co_varnames)