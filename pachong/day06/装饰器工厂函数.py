def func1(*args, **kwargs):  # 接受@func1的参数
    print("装饰器参数：", args, kwargs)

    def func2(func):
        def func3():
            print("kkkkkk")
            return func()

        return func3

    return func2


@func1(2, g=9)
def a():
    print("lllllllll")
    return "xjd"


s = a()
print(s)
