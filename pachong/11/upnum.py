# -*- coding: utf-8 -*-

import random
import time
import requests

proxy_list = []


def get_proxy_list():
    global proxy_list
    print("导入proxy_list...")
    # ip文件可以浏览我上文链接文章“多线程爬虫——抓取代理ip”
    f = open("ip.txt")
    # 从文件中读取的line会有回车，要把\n去掉
    line = f.readline().strip('\n')
    while line:
        proxy_list.append(line)
        line = f.readline().strip('\n')
    f.close()


def start():
    # 总次数和有效次数
    times = 0
    finished_times = 0
    # 无限刷
    while 1:
        user_agent_list = [
            {'Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0)'},
            {'Mozilla/4.0(compatible;MSIE8.0;WindowsNT6.0;Trident/4.0)'},
            {'Mozilla/4.0(compatible;MSIE7.0;WindowsNT6.0)'},
            {'Opera/9.80(WindowsNT6.1;U;en)Presto/2.8.131Version/11.11'},
            {'Mozilla/5.0(WindowsNT6.1;rv:2.0.1)Gecko/20100101Firefox/4.0.1'},
            {'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER'},
            {'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)'},
            {'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0'},
            {'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.3.4000 Chrome/30.0.1599.101 Safari/537.36'},
            {'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 UBrowser/4.0.3214.0 Safari/537.36'},
            {'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5'},
        ]

        referer_list = [
            {'http://blog.csdn.net/dala_da/article/details/79401163'},
            {'http://blog.csdn.net/'},
            {'https://www.sogou.com/tx?query=%E4%BD%BF%E7%94%A8%E7%88%AC%E8%99%AB%E5%88%B7csdn%E8%AE%BF%E9%97%AE%E9%87%8F&hdq=sogou-site-706608cfdbcc1886-0001&ekv=2&ie=utf8&cid=qb7.zhuye&'}
        ]
        # 想要刷的blog的url
        url = 'http://blog.csdn.net/dala_da/article/details/79401163'
        # 随机user_agent和Referer
        header = {'User-Agent': random.choice(user_agent_list),
                  'Referer': random.choice(referer_list)
                  }
        # 依次从proxy_list中取
        ip = proxy_list[times % len(proxy_list)]
        # 设置代理,格式如下
        proxy_ip = 'http://' + ip
        proxy_ips = 'https://' + ip
        proxy = {'https': proxy_ips, 'http': proxy_ip}

        try:
            response = requests.get(url, headers=header, proxies=proxy)
        except:
            # 无响应则print出该代理ip
            print('代理出问题啦:' + proxy["https"])
            time.sleep(0.1)
        else:
            print('已刷%d次,%s') % (finished_times + 1, proxy["https"])
            time.sleep(random.random())
            finished_times += 1

        times += 1
        # 每当所有的代理ip刷过一轮，延时15秒
        if not times % len(proxy_list):
            time.sleep(15)


def readip(proxy_list: list):
    f = open('ip.txt', 'r')
    ip = f.readline().strip()
    while ip:
        proxies = {
            "http": "http://%s" % ip,
            "https": "https://%s" % ip
        }
        proxy_list.append(proxies)
        ip = f.readline().strip()


def upnum(url, proxy: list, header: list):

    for i in range(len(proxy)):
        try:
            res = requests.get(url=url, proxies=proxy[i], headers={'User-Agent': header[random.randint(0, 10)]})
            if res.status_code == 200:
                print("success_%s" % i)
            else:
                print("failed")
        except Exception as e:
            print(e)
            print("failed")
        time.sleep(random.randint(1, 4))


if __name__ == "__main__":
    get_proxy_list()
    start()
"""
123.139.56.238:9999
113.120.63.179:9999
120.26.208.102:88
1.197.16.128:9999
1.197.203.62:9999
113.121.23.242:9999
113.120.63.179:9999
121.17.174.121:9797
117.64.250.201:808
14.20.235.44:808
222.89.32.168:9999
211.101.154.105:43598
140.143.48.49:1080
1.197.204.15:9999
183.136.177.77:3128
220.249.149.46:9999
182.92.105.136:3128
121.233.251.98:9999
1.198.72.216:9999
58.244.52.235:8080
218.241.219.226:9999
1.198.73.16:9999
182.34.35.127:9999
114.230.24.233:9999
"""
