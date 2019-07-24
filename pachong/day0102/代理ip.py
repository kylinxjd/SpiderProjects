import json
import random
import threading

import requests
from lxml import etree
from queue import Queue

ipqueue = Queue()


def get_ip(page):
    global ipqueue
    for p in range(1, page):
        url = 'https://www.xicidaili.com/nn/%s' % p

        head = {
            'Referer': 'https://www.xicidaili.com/nn/',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
        }
        heads = [
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
            "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
        ]

        res = requests.get(url=url, headers=head)

        html_doc = etree.HTML(res.text, etree.HTMLParser())

        ret1 = html_doc.xpath('//table/tr/td[2]/text()')
        ret2 = html_doc.xpath('//table/tr/td[3]/text()')
        ret3 = html_doc.xpath('//table/tr/td[6]/text()')

        print(ret1)
        print(ret2)
        print(ret3)

        for ip, port, protocol in zip(ret1, ret2, ret3):
            proxy = {
                protocol: "%s://%s:%s" % (protocol, ip, port)
            }
            try:
                res = requests.get(url='https://www.baidu.com',
                                   headers={
                                       'User-Agent': heads[random.randint(0, 10)]
                                   },
                                   proxies=proxy)
                print(res.content)
                print(res.status_code)
            except Exception as e:
                print("sss", e)
                print("失败")
            else:
                print(proxy)
                print("成功")
                ipqueue.put(json.dumps(proxy))


def save():
    with open('代理IP.txt', 'a+') as f:
        while True:
            if ipqueue.qsize() == 0:
                break
            try:
                pro = ipqueue.get()
                f.write(pro)
            except Exception as e:
                print(e)
                raise Exception("队列空")
            else:
                print(pro)


if __name__ == '__main__':
    get_ip(2)
    while True:
        if ipqueue.qsize() == 0:
            break
        try:
            pro = ipqueue.get()
        except Exception as e:
            print(e)
            raise Exception("队列空")
        else:
            print(pro, end=',')
            print('')
    # threading.Thread(target=)
