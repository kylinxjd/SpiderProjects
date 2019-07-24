def wapper(func):
    print("aaaaaaaaaaaaaaaaaaa")

    def inner(*args, **kwargs):
        print("KKKKKKKKKKKKKKKKKKKKKKKKK")
        print(args)
        print(kwargs)
        return func(*args, **kwargs)

    print("xxxxxxxxxxxxxxxxxxxxxxxxx")
    return inner


@wapper
def a(num1, num2=4):
    print("ssss")
    print(num1+4)
    return "xjd"


print(a(3, num2=3))
