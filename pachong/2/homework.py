import threading

import pymongo
import random
from time import sleep

import requests
from bs4 import BeautifulSoup


def get_data(page: int, city, db):
    # proxy = {
    #     "http": "http://61.135.155.82:443"
    # }

    proxy = [
        {
            "http": "http://58.219.63.71:9999"
        },
        {
            "http": "http://61.135.155.82:443"
        }
    ]

    head = {
        'pragma': 'no-cache',
        'referer': 'https://wuhan.zu.fang.com/',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
    }

    for p in range(page, page + 3):

        print("第%s页-----------------" % p)

        # mongodb集合
        coll = db['wuhan_page_%s' % p]

        # url = 'https://%s.zu.fang.com/house/i3%s/' % (city, p)
        url = 'https://%s.zu.fang.com/house/i3%s/' % (city, p)

        try:
            # 一级页面
            res = requests.get(url=url, headers=head, proxies=proxy[random.randint(0, 1)])
        except Exception as e:
            print(e)
            continue

        # 随机频率
        sleep(random.randint(500, 2500) / 1000)

        if res.status_code != 200:
            print(res.status_code)
            return

        html = res.text

        soup = BeautifulSoup(html, 'html.parser')

        obj = soup.select('dl[class="list hiddenMap rel"] dd[class="info rel"] p[class="title"] a')

        # 一个页面的数据
        data_list = []

        for a in obj:
            a_url = a.attrs['href']
            # 二级页面
            detail_url = 'https://wuhan.zu.fang.com%s' % a_url
            try:
                res2 = requests.get(url=detail_url, headers=head, proxies=proxy[random.randint(0, 1)])
            except Exception as e:
                print(e)
                continue
            if res2.status_code != 200:
                print(res.status_code)
                continue
            sleep(random.randint(500, 3000) / 1000)
            detail_html = res2.text
            soup_detail = BeautifulSoup(detail_html, 'html.parser')
            # 获取详情
            obj = soup_detail.select('div[class="tab-cont-right"] div[class="tr-line clearfix zf_new_title"] i')
            obj2 = soup_detail.select('div[class="tab-cont-right"] div[class="tr-line clearfix"] div[class="tt"]')
            obj3 = soup_detail.select(
                'div[class="tab-cont-right"] div[class="tr-line"] div[class="trl-item2 clearfix"] div[class="rcont"] a')
            obj4 = soup_detail.select('p[class="gray9 fybh-zf"] span')
            # print("价格 ", obj[0].get_text())
            # print("出租方式 ", obj2[0].get_text())
            # print("户型 ", obj2[1].get_text())
            # print("建筑面积 ", obj2[2].get_text())
            # print("朝向 ", obj2[3].get_text())
            # print("楼层 ", obj2[4].get_text())
            # print("装修 ", obj2[5].get_text())
            # print("小区 ", obj3[0].get_text())
            # print("地址 ", obj3[-1].get_text())
            # print("更新时间 ", obj4[-1].get_text().split(' ')[-1])
            data = {
                '价格': obj[0].get_text(),
                '出租方式': obj2[0].get_text(),
                '户型': obj2[1].get_text(),
                '建筑面积': obj2[2].get_text(),
                '朝向': obj2[3].get_text(),
                '楼层': obj2[4].get_text(),
                '装修': obj2[5].get_text(),
                '小区': obj3[0].get_text(),
                '地址': obj3[-1].get_text(),
                '更新时间': obj4[-1].get_text().split(' ')[-1],
            }
            print(data['地址'])
            data_list.append(data)
        coll.insert(data_list)


if __name__ == '__main__':
    client = pymongo.MongoClient("127.0.0.1", 27017)
    db = client['house']
    # coll = db['shanghai']
    # get_data(9, 'hz', db)
    thread1 = threading.Thread(target=get_data, args=(1, 'wuhan', db))  # 线程对象.
    thread2 = threading.Thread(target=get_data, args=(4, 'wuhan', db))  # 线程对象.
    thread3 = threading.Thread(target=get_data, args=(7, 'wuhan', db))  # 线程对象.
    thread4 = threading.Thread(target=get_data, args=(10, 'wuhan', db))  # 线程对象.
    thread5 = threading.Thread(target=get_data, args=(13, 'wuhan', db))  # 线程对象.
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()
    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()
    thread5.join()
