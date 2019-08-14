# import sys
#
#
# def fibonacci(n):  # 生成器函数 - 斐波那契
#     a, b, counter = 0, 1, 0
#     while True:
#         if counter > n:
#             return
#         yield a
#         a, b = b, a + b
#         counter += 1
#
#
# f = fibonacci(10)  # f 是一个迭代器，由生成器返回生成
#
# while True:
#     try:
#         print(next(f), end=" ")
#     except StopIteration:
#         sys.exit()
# ---------------------------------------------------------------------------
def send_generator():
    print("######################")
    content = yield 1
    # content就是同send传递过来的
    print('=======', content)
    print("@@@@@@@@@@@@@@@@@@@@@@")
    yield 2


g = send_generator()
ret = g.__next__()
print('============', ret)
ret = g.send('hello')  # send的效果和next一样
print('============', ret)

# send 获取下一个值的效果和next基本一致
# 只是在获取下一个值的时候，给上一yield的位置传递一个数据
# 使用send的注意事项
# 第一次使用生成器的时候 是用next获取下一个值
# 最后一个yield不能接受外部的值
# ========================================================================
# def averager():
#     total = 0.0
#     count = 0
#     average = None
#     while True:
#         term = yield average
#         total += term
#         count += 1
#         average = total/count
#
#
# g_avg = averager()
# print(next(g_avg))
# print(g_avg.send(10))
# print(g_avg.send(30))
# print(g_avg.send(5))
#
# # 计算移动平均值(1)

