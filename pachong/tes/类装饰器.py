class A(object):
    def __init__(self, func):
        print("__init__")
        self.func = func

    def __call__(self, *args, **kwargs):
        # 接收参数
        print("__call__")
        print(args)
        print(kwargs)
        print("__call__")
        self.func(*args, **kwargs)


class B(object):
    def __init__(self, *args, **kwargs):
        print("__init__")
        print(args)
        print(kwargs)
        print("__init__")

    def __call__(self, func):
        print("__call__")

        def inner(*args, **kwargs):
            print(args)
            print(kwargs)
            return func(*args, **kwargs)

        return inner

# @A
# def hello(name, age=12):
#     print("hello")
#     print(name)
#     print(age)
#     print("hello")


@B('xiaowang', age=12)
def hello2(name, age=15):
    print("hello2")
    print(name)
    print(age)
    print("hello2")


# hello('xiaowang', age=16)
# __init__
# __call__
# ('xiaowang',)
# {'age': 16}
# __call__
# hello
# xiaowang
# 16
# hello

hello2('xiaowang', age=16)
# __init__
# ('xiaowang',)
# {'age': 12}
# __init__
# __call__
# ('xiaowang',)
# {'age': 16}
# hello2
# xiaowang
# 16
# hello2
