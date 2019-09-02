# -*- coding: utf-8 -*-
"""
Created on Sat Mar 03 19:06:18 2018
@author: Administrator
"""

import re
import requests
import time
from threading import Thread
from threading import Lock
from queue import Queue

# 从西刺抓下来的所有代理ip
all_find_list = []
# 将所有抓到的代理压入队列，四个线程可以从队列中获取代理ip
gaoni_queue = Queue()
# 能够成功连接的代理ip
success_list = []

lock = Lock()


def get_proxy(checking_ip):
    # 根据得到的代理ip，设置proxy的格式
    proxy_ip = 'http://' + checking_ip
    proxy_ips = 'https://' + checking_ip
    proxy = {'https': proxy_ips, 'http': proxy_ip}
    return proxy


def checking_ip():
    global gaoni_queue
    global success_list
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
    }

    while 1:
        # 若从队列1秒内无法获得代理ip，说明所有代理均已检测完成，抛出Empty异常
        try:
            check_ip = gaoni_queue.get(True, 1)
        except:
            gaoni_queue.task_done()
            break

        proxy = get_proxy(check_ip)
        url = 'https://www.csdn.net/'
        # 使用上面的url，测试代理ip是否能够链接
        try:
            page = requests.get(url, headers=headers, proxies=proxy)
        except:
            lock.acquire()
            print(check_ip, '失败')
            lock.release()
        else:
            lock.acquire()
            print(check_ip, '成功')
            success_list.append(check_ip)
            lock.release()


def get_all():
    headers = {
        'User-Agent': 'Mozilla/5.0(WindowsNT6.1;rv:2.0.1)Gecko/20100101Firefox/4.0.1'}
    global all_find_list
    # for i in range(18, 20):
    # 从xici网站的高匿页面获取ip
    url = 'http://www.xicidaili.com/nn/45'

    # url = 'http://ip.zdaye.com/dayProxy/ip/313918.html'
    r = requests.get(url, headers=headers)
    data = r.text
    # 抓取所需数据的正则表达式
    p = r'<td>(.*?)</td>\s+<td>(.*?)</td>\s+<td>\s+(.*?)\s+</td>\s+<td class="country">(.*?)</td>'

    # <br>183.63.101.62:55555@
    # p = r'<br>'
    find_list = re.findall(p, data)
    all_find_list += find_list

    # 将ip地址与端口组成规定格式
    for row in all_find_list:
        ip = row[0] + ':' + row[1]
        gaoni_queue.put(ip)


if __name__ == '__main__':
    get_all()
    print(gaoni_queue.qsize())
    thread_1 = Thread(target=checking_ip)
    thread_2 = Thread(target=checking_ip)
    thread_3 = Thread(target=checking_ip)
    thread_4 = Thread(target=checking_ip)
    thread_1.start()
    thread_2.start()
    thread_3.start()
    thread_4.start()
    thread_1.join()
    thread_2.join()
    thread_3.join()
    thread_4.join()
    # 182.34.35.172:9999
    f = open("ip.txt", "w")
    for row in success_list:
        f.write(row + '\n')
    f.close()
