def wapper(func):
    def inner(*args, **kwargs):
        print("执行function——a之前")
        print("传递的参数")
        print(args)
        print(kwargs)

        return func(*args, **kwargs)

    return inner


@wapper
def a(num1, num2=5):
    print("执行function——a")
    print(num1)
    print(num2)


def b():
    print("执行function——b")


if __name__ == '__main__':
    a(2, num2=56)
