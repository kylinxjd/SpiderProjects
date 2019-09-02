class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


# 实例化自定义迭代器
myclass = MyNumbers()
# 创建迭代器对象
myiter = iter(myclass)

for i in myiter:
    print(i, end="  ")

# list1 = [1, 2, 3, 4, 5]
#
# # 通过iter创建迭代器对象
# it = iter(list1)
# # 通过next()函数依次遍历迭代器
# # print(next(it))
# # print(next(it))
# # print(next(it))
# # print(next(it))
# # print(next(it))
#
# for i in it:
#     print(i, end="  ")
