def test(Hello, world):
    pass


if __name__ == "__main__":
    code_obj = test.__code__
    print(code_obj.co_varnames[0]+','+code_obj.co_varnames[1]+'!')