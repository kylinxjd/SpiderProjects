import csv
import re
import threading

import pymongo
import random
from time import sleep

import requests
from bs4 import BeautifulSoup


def get_data(key, page, head, proxy, coll):
    # url = http://search.dangdang.com/?key=python&act=input&page_index=4

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

    for p in range(page * 3 - 2, page * 3 + 1):

        print("第%s页-----------------" % p)

        url = 'http://search.dangdang.com/?key=%s&act=input&page_index=%s' % (key, p)
        # 获取一级页面text
        try:
            res = requests.get(url=url, headers=head)
        except Exception as e:
            print(e)
            continue
        html = res.text
        sleep(random.randint(100, 1000) / 1000)
        # 获取二级页面url
        soup = BeautifulSoup(html, 'html.parser')

        detail_url_list = soup.select('p[class="name"] a')

        data_list = []

        for a in detail_url_list:
            head['User-Agent'] = heads[random.randint(0, 10)]
            detail_url = a.attrs['href']
            print(detail_url)
            # 获取二级页面详情
            try:
                res2 = requests.get(url=detail_url, headers=head, proxies=proxy[random.randint(0, 70)])
            except Exception as e:
                print(e)
                continue
            detail_html = res2.text
            sleep(random.randint(0, 180) / 1000)
            soup2 = BeautifulSoup(detail_html, 'html.parser')
            # 开 本：16开纸 张：胶版纸包 装：平装-胶订是否套装：否国际标准书号ISBN：9787121341366  等
            obj = soup2.select('ul[class="key clearfix"] li')
            # 作者:（加）Dusty Phillips（达斯帝·菲利普斯）出版社:电子工业出版社出版时间:2018年06月  等
            obj1 = soup2.select('div[class="messbox_info"] span')
            # 标题书名
            obj2 = soup2.select('div[class="sale_box_left"] div[class="name_info"] h1')
            # 价格
            obj3 = soup2.select('p[id="dd-price"]')
            dic = {}
            for o in obj:
                txt = o.get_text().strip()
                if txt:
                    txt = re.sub(r' ', '', txt)
                    txt_list = txt.split('：')
                    dic[txt_list[0]] = txt_list[1]
            for o in obj1:
                txt = o.get_text().strip()
                if re.search(r'\d+条评论', txt):
                    comments = re.search(r'(\d+)条评论', txt).group(1)
                    dic['评论数'] = comments
                elif re.search(r':', txt):
                    txt_list = txt.split(':')
                    dic[txt_list[0]] = txt_list[1]
            if not all([obj2, obj3]):
                continue
            dic['书名'] = obj2[0].attrs['title'].strip()
            dic['价格'] = obj3[0].get_text().strip().split('¥')[1].strip()

            data = {
                "bookName": dic.get('书名', '---'),
                "author": dic.get('作者', '---'),
                "publish": dic.get('出版社', '---'),
                "publishTime": dic.get('出版时间', '---'),
                "price": dic.get('价格', '---'),
                "ISBN": dic.get('国际标准书号ISBN', '---'),
                "comments": dic.get('评论数', '---'),
                "paperType": dic.get('纸张', '---'),
                "package": dic.get('包装', '---'),
                # 是否套装
                "isSuit": dic.get('是否套装', '---'),
                "category": dic.get('所属分类', '---'),
            }
            print(data)
            data_list.append(data)
        #     加锁写csv
        mutex.acquire(timeout=5)
        # 写入mongodb
        # coll.insert(data_list)

        # 写入csv
        fieldnames = ['bookName', 'author', 'publish', 'publishTime', 'price',
                      'ISBN', 'comments', 'paperType',
                      'package', 'isSuit', 'category']
        with open('dangdang.csv', 'a+', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            # # 写第一行表头
            # writer.writeheader()
            writer.writerows(data_list)
        mutex.locked()


if __name__ == '__main__':
    # 线程锁
    mutex = threading.Lock()

    key = 'hadoop'
    header = {
        'Pragma': 'no-cache',
        'Referer': 'http://search.dangdang.com/?key=%s&act=input' % key,
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
        'Cookie': '__permanent_id=20190806184835961303725577737149416; NTKF_T2D_CLIENTID=guest4135C948-2259-8392-7CE7-668BD1D788E2; producthistoryid=25312917%2C1340897421%2C1517597547%2C27785908%2C25859443%2C25071121%2C25301983%2C1460516830%2C24003316%2C26436548; permanent_key=20190815183807474926637434f82ec8; from=422-kw-1-%C6%B7%C5%C6%B4%CA_%C6%B7%C5%C6%B4%CA-%BA%CB%D0%C4_%B5%B1%B5%B1; order_follow_source=P-422-kw-1%7C%231%7C%23www.baidu.com%252Fbaidu.php%253Fsc.K00000KbUiqGbb95aPKBRtqCeLulT4C-pSQmCXUzNOmJPghciot4s4Zw_8IWY_v1SYjbXalqr%7C%230-%7C-; ddscreen=2; __visit_id=20190823155618323227353435103532682; __out_refer=1566546978%7C!%7Cwww.baidu.com%7C!%7C%25E5%25BD%2593%25E5%25BD%2593; __ddc_1d=1566546978%7C!%7C_utm_sem_id%3D16202048; __ddc_24h=1566546978%7C!%7C_utm_sem_id%3D16202048; __ddc_15d=1566546978%7C!%7C_utm_sem_id%3D16202048; __ddc_15d_f=1566546978%7C!%7C_utm_sem_id%3D16202048; dest_area=country_id%3D9000%26province_id%3D111%26city_id%3D0%26district_id%3D0%26town_id%3D0; search_passback=07b8352315f3cac4759c5f5d00000000; pos_9_end=1566547061545; pos_0_end=1566547061577; ad_ids=2760400%7C%232; pos_0_start=1566547062854; __rpm=s_112100...1566547040029%7Cs_82229...1566547082622; __trace_id=20190823155806055122404750917717661'
    }
    ip_proxies = [
        {"http": "http://61.135.155.82:443"},
        {"HTTP": "HTTP://123.163.97.136:9999"},
        {"HTTP": "HTTP://171.12.112.68:9999"},
        {"HTTP": "HTTP://114.239.29.121:9999"},
        {"HTTP": "HTTP://163.204.242.244:9999"},
        {"HTTPS": "HTTPS://1.198.73.139:9999"},
        {"HTTP": "HTTP://117.95.195.156:9999"},
        {"HTTP": "HTTP://171.11.28.198:9999"},
        {"HTTPS": "HTTPS://114.239.144.6:808"},
        {"HTTPS": "HTTPS://117.64.149.5:808"},
        {"HTTPS": "HTTPS://120.83.108.13:9999"},
        {"HTTP": "HTTP://183.166.138.30:9999"},
        {"HTTP": "HTTP://120.83.104.225:9999"},
        {"HTTPS": "HTTPS://120.83.108.37:9999"},
        {"HTTPS": "HTTPS://58.253.155.40:9999"},
        {"HTTP": "HTTP://117.95.214.78:9999"},
        {"HTTP": "HTTP://1.197.16.205:9999"},
        {"HTTP": "HTTP://112.85.165.214:9999"},
        {"HTTPS": "HTTPS://120.83.104.195:9999"},
        {"HTTP": "HTTP://114.239.199.54:9999"},
        {"HTTP": "HTTP://114.239.147.194:9999"},
        {"HTTP": "HTTP://171.11.32.15:9999"},
        {"HTTPS": "HTTPS://114.239.151.20:808"},
        {"HTTP": "HTTP://59.57.38.113:9999"},
        {"HTTP": "HTTP://1.198.72.150:9999"},
        {"HTTP": "HTTP://120.83.110.91:9999"},
        {"HTTPS": "HTTPS://117.28.97.106:9999"},
        {"HTTPS": "HTTPS://117.64.149.228:808"},
        {"HTTPS": "HTTPS://58.253.157.14:9999"},
        {"HTTPS": "HTTPS://182.34.34.211:9999"},
        {"HTTPS": "HTTPS://163.204.242.242:9999"},
        {"HTTPS": "HTTPS://113.124.92.89:9999"},
        {"HTTP": "HTTP://171.11.179.48:9999"},
        {"HTTP": "HTTP://112.85.170.188:9999"},
        {"HTTP": "HTTP://114.239.251.106:9999"},
        {"HTTP": "HTTP://112.87.71.42:9999"},
        {"HTTP": "HTTP://163.204.242.250:9999"},
        {"HTTP": "HTTP://171.11.178.221:9999"},
        {"HTTP": "HTTP://60.13.42.102:9999"},
        {"HTTPS": "HTTPS://163.204.242.60:9999"},
        {"HTTP": "HTTP://60.13.42.248:9999"},
        {"HTTP": "HTTP://60.13.42.225:9999"},
        {"HTTPS": "HTTPS://163.204.247.100:9999"},
        {"HTTP": "HTTP://1.198.72.194:9999"},
        {"HTTP": "HTTP://117.95.192.14:9999"},
        {"HTTP": "HTTP://117.95.214.29:9999"},
        {"HTTPS": "HTTPS://117.95.232.203:9999"},
        {"HTTPS": "HTTPS://1.198.72.129:9999"},
        {"HTTP": "HTTP://58.253.154.102:9999"},
        {"HTTPS": "HTTPS://120.83.99.25:9999"},
        {"HTTP": "HTTP://123.169.123.214:9999"},
        {"HTTP": "HTTP://223.215.176.126:808"},
        {"HTTP": "HTTP://114.239.150.228:808"},
        {"HTTP": "HTTP://171.13.136.55:9999"},
        {"HTTP": "HTTP://163.204.247.178:9999"},
        {"HTTP": "HTTP://182.35.82.163:9999"},
        {"HTTP": "HTTP://163.204.243.203:9999"},
        {"HTTP": "HTTP://163.204.242.252:9999"},
        {"HTTP": "HTTP://112.87.70.195:9999"},
        {"HTTPS": "HTTPS://1.197.203.62:9999"},
        {"HTTPS": "HTTPS://183.166.86.158:9999"},
        {"HTTP": "HTTP://112.85.165.5:9999"},
        {"HTTP": "HTTP://112.85.169.2:9999"},
        {"HTTP": "HTTP://120.83.96.29:9999"},
        {"HTTP": "HTTP://120.83.110.240:9999"},
        {"HTTP": "HTTP://112.85.131.107:9999"},
        {"HTTPS": "HTTPS://123.101.110.140:36689"},
        {"HTTP": "HTTP://60.13.42.209:9999"},
        {"HTTP": "HTTP://1.197.204.130:9999"},
        {"HTTPS": "HTTPS://1.197.203.225:9999"},
        {"HTTP": "HTTP://58.253.154.230:9999"},
        {"HTTP": "HTTP://163.204.245.116:9999"},
        {"HTTP": "HTTP://59.57.148.78:9999"},
        {"HTTP": "HTTP://49.70.32.81:9999"},
        {"HTTP": "HTTP://123.169.35.39:9999"},
        {"HTTP": "HTTP://1.197.204.208:9999"},
        {"HTTP": "HTTP://60.166.87.106:808"},
        {"HTTP": "HTTP://120.83.120.144:9999"},
        {"HTTPS": "HTTPS://1.198.73.148:9999"},
        {"HTTP": "HTTP://163.204.242.12:9999"},
        {"HTTPS": "HTTPS://122.193.245.98:9999"},
        {"HTTP": "HTTP://123.163.122.188:9999"},
        {"HTTPS": "HTTPS://120.83.109.194:9999"},
        {"HTTP": "HTTP://112.85.170.88:9999"},
        {"HTTP": "HTTP://60.216.101.46:59351"},
        {"HTTPS": "HTTPS://113.121.23.15:9999"},
        {"HTTP": "HTTP://113.120.33.62:9999"},
        {"HTTPS": "HTTPS://182.35.86.65:9999"},
        {"HTTPS": "HTTPS://112.87.68.234:9999"},
        {"HTTPS": "HTTPS://182.34.33.63:9999"},
        {"HTTPS": "HTTPS://163.204.246.123:9999"},
        {"HTTP": "HTTP://163.204.241.0:9999"},
        {"HTTP": "HTTP://120.83.121.97:9999"},
        {"HTTP": "HTTP://163.204.93.243:9999"},
        {"HTTP": "HTTP://113.120.35.154:9999"},
        {"HTTPS": "HTTPS://222.89.32.176:8070"},
        {"HTTPS": "HTTPS://222.189.191.136:9999"},
        {"HTTP": "HTTP://163.204.241.95:9999"},
        {"HTTP": "HTTP://182.35.83.202:9999"},
        {"HTTPS": "HTTPS://163.204.243.170:9999"},
        {"HTTPS": "HTTPS://163.204.247.147:9999"},
    ]
    # MongoDB设置
    client = pymongo.MongoClient("127.0.0.1", 27017)
    db = client['dangdang']
    coll = db[key]
    thread_list = []
    for i in range(1, 30):
        t = threading.Thread(target=get_data, args=(key, i, header, ip_proxies, coll))
        t.start()
        thread_list.append(t)
    for th in thread_list:
        th.join()


