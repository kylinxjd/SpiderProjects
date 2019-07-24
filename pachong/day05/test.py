import datetime
import time

import pymongo
import random

import requests
from bs4 import BeautifulSoup

# url = 'https://sh.zu.fang.com/chuzu/3_354858667_1.htm'

proxy = {
    "http": "http://58.219.63.71:9999"
}

head = {
    'pragma': 'no-cache',
    'referer': 'https://sh.zu.fang.com/',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
}

head2 = {
    'Pragma': 'no-cache',
    'Referer': 'http://search.dangdang.com/?key=python&act=input',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
}

res = requests.get(url='http://search.dangdang.com/?key=python&act=input', headers=head2, proxies=proxy)

print(res.text)


# # 创建链接对象，第一个参数是IP地址，第二个参数是端口，默认27017
# client = pymongo.MongoClient("127.0.0.1", 27017)
# # 链接数据库
# db = client['pymongo']
# # 创建文档
# coll = db['mongotest']

# data_list = [
#     {'name': 'mary', 'age': 24},
#     {'name': 'tom', 'age': 22},
#     {'name': 'bob', 'age': 23},
#     {'name': 'tom3', 'age': 24},
#     {'name': 'lisa', 'age': 31},
#     {'name': 'lili', 'age': 21},
# ]
#
# coll.insert_many(documents=data_list)


data_list = [
    {'name': 'python', 'age': 24},
    {'name': 'java', 'age': 24},
    {'name': 'C', 'age': 24}
]
# coll.insert(doc_or_docs=data_list)
# ret = coll.find_one(filter={'name': 'tom'})
# print("查询一条数据")
# print(ret)
# rets = coll.find()
# print("查询多条数据")
# for i in rets:
#     print(i)

# age大于32
# print("age大于32")
# ret1 = coll.find({'age': {'$gt': 23}})
# for i in ret1:
#     print(i)
# # age大于等于32
# print("age大于等于32")
# ret1 = coll.find({'age': {'$gte': 23}})
# for i in ret1:
#     print(i)
# # 年龄小于32
# print("年龄小于23")
# ret1 = coll.find({'age': {'$lt': 23}})
# for i in ret1:
#     print(i)
# # age不等于32
# print("age不等于32")

# ret1 = coll.find({})
# for i in ret1:
#     print(i)
# # 删除age=23的第一条
# print("ssssssssssssssssssssssssssss")
# coll.delete_one({'age': 23})
# ret1 = coll.find({})
# for i in ret1:
#     print(i)
#
# data = {
#     'name': 'mary',
#     'age': 23
# }
# coll.insert(data)
# coll.insert(doc_or_docs=data)

# coll.update(spec={'name':'C'}, document={'$set':{'age':12}})

# from concurrent.futures import ThreadPoolExecutor
# import threading
# import time
#
#
# # 定义一个准备作为线程任务的函数
# def action(max):
#     my_sum = 0
#     for i in range(max):
#         print(threading.current_thread().name + '  ' + str(i))
#         my_sum += i
#     return my_sum
#
#
# s = time.time()
# print(s)
# # 创建一个包含2条线程的线程池
# with ThreadPoolExecutor(max_workers=2) as pool:
#     # 向线程池提交一个task, 50会作为action()函数的参数
#     future1 = pool.submit(action, 50)
#     # 向线程池再提交一个task, 100会作为action()函数的参数
#     future2 = pool.submit(action, 100)
#
#
#     def get_result(future):
#         print(future.result())
#
#
#     # 为future1添加线程完成的回调函数
#     future1.add_done_callback(get_result)
#     # 为future2添加线程完成的回调函数
#     future2.add_done_callback(get_result)
#     print('--------------')
# #     0.004986286163330078
#       0.0019948482513427734
#       0.005982875823974609
# print(time.time())
# if future1.done() and future2.done():
#     print(time.time() - s)

# t1 = threading.Thread(target=action, args=[50])
# t2 = threading.Thread(target=action, args=[100])
# t3 = threading.Thread(target=action, args=[200])
# t4 = threading.Thread(target=action, args=[300])
# t1.start()
# t2.start()
# t3.start()
# t4.start()
# t1.join()
# t2.join()
# t3.join()
# t4.join()
# print(time.time())
# print(time.time() - s)

# t = time.time()
# print(int(round(t * 1000)))
#
# print(1563528130327-1563528131080)
# print(1563528410349-1563528130327)
#
# print(1563528130327-1563528131080)
# print(1563528241418-1563528130327)
#
# # cgitm: 1563528131080
# # clitm: 1563528130327
# # comtm: 1563534703045
#
# print(1563528130327-1563528131080)
# print(1563534703045-1563528130327)
