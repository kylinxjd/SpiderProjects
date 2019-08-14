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
                res2 = requests.get(url=detail_url, headers=head, proxies=proxy[random.randint(0, 80)])
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

            # obj1 = soup2.select('div[class="sale_box_left"] div[class="name_info"] h1')
            # author_obj = soup2.select('div[class="messbox_info"] span a[dd_name="作者"]')
            # publish_house_obj = soup2.select('div[class="messbox_info"] span a[dd_name="出版社"]')
            # publish_time_obj = soup2.select('div[class="messbox_info"] span')
            # price_obj = soup2.select('p[id="dd-price"]')
            # isbn_obj = soup2.select('ul[class="key clearfix"] li')
            # try:
            #     # 书名
            #     if not obj1:
            #         continue
            #     bookname = obj1[0].attrs['title']
            #     # 作者
            #     if not author_obj:
            #         author = '---'
            #     elif len(author_obj) > 1:
            #         # 外国作者
            #         author = ''
            #         for auth in author_obj[:-1]:
            #             author += auth.get_text() + ' '
            #         author += '(' + author_obj[-1].get_text() + ')'
            #     else:
            #         # 中国作者
            #         author = author_obj[0].get_text()
            #     # 出版社
            #     if not publish_house_obj:
            #         publish = '---'
            #     else:
            #         publish = publish_house_obj[0].get_text()
            #     # 出版时间
            #     if len(publish_time_obj) > 2:
            #         publish_time = publish_time_obj[2].get_text().strip().split(':')[1]
            #     else:
            #         publish_time = '---'
            #
            #     # 价格
            #     price = price_obj[0].get_text().split('¥')[1]
            #
            #     # isbn
            #     isbn = ''
            #     for isb in isbn_obj:
            #         if "国际标准书号ISBN" == isb.get_text().strip().split('：')[0]:
            #             isbn = isb.get_text().strip().split('：')[1]
            #             break
            #     if not isbn:
            #         isbn = "---"
            #
            #     data = {
            #         "book_name": bookname,
            #         "author": author,
            #         "publish": publish,
            #         "publish_time": publish_time,
            #         "price": price.strip(),
            #         "ISBN": isbn
            #     }
            #     print(data['book_name'])
            #     data_list.append(data)
            # except Exception as e:
            #     print(e)
            #     continue

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

    key = 'java'
    header = {
        'Pragma': 'no-cache',
        'Referer': 'http://search.dangdang.com/?key=%s&act=input' % key,
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
        'Cookie': 'from=P-295132-217563_64_0__1; order_follow_source=P-295132-2%7C%231%7C%23c.duomai.com%252Ftrack.php%253Fsite_id%253D217563%2526aid%253D64%2526euid%253D%2526t%253Dhttp%25253a%25252f%25252fwww.dangdang.com%25252f%7C%230%7C%233BlvQv02FQCb-%7C-; ddscreen=2; __permanent_id=20190720154036144174983416090664471; __visit_id=20190720154036146845894385985963627; __out_refer=1563608436%7C!%7Cc.duomai.com%7C!%7C; __ddc_1d=1563608436%7C!%7C_ddclickunion%3DP-295132-217563_64_0__1; __ddc_24h=1563608436%7C!%7C_ddclickunion%3DP-295132-217563_64_0__1; __ddc_15d=1563608436%7C!%7C_ddclickunion%3DP-295132-217563_64_0__1; __ddc_15d_f=1563608436%7C!%7C_ddclickunion%3DP-295132-217563_64_0__1; __rpm=%7Cmix_317715...1563608443674; search_passback=91da83bf7b229c4f7fc5325d00000000; __trace_id=20190720154047317168208131370294392; dest_area=country_id%3D9000%26province_id%3D111%26city_id%3D0%26district_id%3D0%26town_id%3D0; pos_9_end=1563608447466; pos_0_end=1563608447563; pos_0_start=1563608448650'
    }
    ip_proxies = [
        {"http": "http://61.135.155.82:443"},
        {"HTTP": "HTTP://163.204.244.40:9999"},
        {"HTTPS": "HTTPS://163.204.241.226:9999"},
        {"HTTPS": "HTTPS://113.120.35.221:9999"},
        {"HTTPS": "HTTPS://163.204.240.180:9999"},
        {"HTTPS": "HTTPS://222.94.151.2:808"},
        {"HTTP": "HTTP://163.204.241.72:9999"},
        {"HTTP": "HTTP://163.204.245.60:9999"},
        {"HTTP": "HTTP://120.83.108.251:9999"},
        {"HTTP": "HTTP://163.204.247.12:9999"},
        {"HTTP": "HTTP://163.204.247.115:9999"},
        {"HTTP": "HTTP://163.204.240.154:9999"},
        {"HTTP": "HTTP://123.163.96.87:9999"},
        {"HTTP": "HTTP://123.163.122.132:9999"},
        {"HTTP": "HTTP://60.13.42.123:9999"},
        {"HTTPS": "HTTPS://120.83.105.175:9999"},
        {"HTTPS": "HTTPS://120.83.97.10:9999"},
        {"HTTPS": "HTTPS://182.35.82.192:9999"},
        {"HTTP": "HTTP://60.13.42.124:9999"},
        {"HTTP": "HTTP://182.34.32.109:9999"},
        {"HTTPS": "HTTPS://182.35.87.203:9999"},
        {"HTTPS": "HTTPS://112.85.131.42:9999"},
        {"HTTPS": "HTTPS://112.85.149.113:9999"},
        {"HTTP": "HTTP://112.85.131.84:9999"},
        {"HTTP": "HTTP://183.166.103.116:9999"},
        {"HTTP": "HTTP://182.34.37.119:9999"},
        {"HTTP": "HTTP://182.35.83.150:9999"},
        {"HTTPS": "HTTPS://223.241.118.106:8010"},
        {"HTTP": "HTTP://163.204.244.126:9999"},
        {"HTTP": "HTTP://112.87.70.105:9999"},
        {"HTTPS": "HTTPS://60.13.42.109:9999"},
        {"HTTP": "HTTP://60.13.42.200:9999"},
        {"HTTP": "HTTP://112.87.68.95:9999"},
        {"HTTPS": "HTTPS://113.121.23.228:40921"},
        {"HTTPS": "HTTPS://27.43.190.247:9999"},
        {"HTTPS": "HTTPS://182.35.85.13:9999"},
        {"HTTPS": "HTTPS://112.85.130.152:9999"},
        {"HTTP": "HTTP://163.204.241.34:9999"},
        {"HTTPS": "HTTPS://183.166.96.213:9999"},
        {"HTTPS": "HTTPS://113.121.23.116:9999"},
        {"HTTPS": "HTTPS://36.249.119.43:9999"},
        {"HTTPS": "HTTPS://113.121.20.214:9999"},
        {"HTTP": "HTTP://123.163.97.185:9999"},
        {"HTTP": "HTTP://113.121.20.53:9999"},
        {"HTTP": "HTTP://112.85.168.52:9999"},
        {"HTTP": "HTTP://113.86.151.149:8118"},
        {"HTTPS": "HTTPS://60.13.42.250:9999"},
        {"HTTP": "HTTP://58.253.154.103:9999"},
        {"HTTP": "HTTP://120.83.101.49:9999"},
        {"HTTP": "HTTP://123.163.97.183:9999"},
        {"HTTPS": "HTTPS://1.197.204.162:9999"},
        {"HTTP": "HTTP://171.212.91.173:61234"},
        {"HTTPS": "HTTPS://163.204.247.157:9999"},
        {"HTTPS": "HTTPS://122.193.244.72:9999"},
        {"HTTPS": "HTTPS://123.163.97.63:9999"},
        {"HTTPS": "HTTPS://123.163.97.64:9999"},
        {"HTTPS": "HTTPS://1.197.16.94:9999"},
        {"HTTPS": "HTTPS://182.35.82.12:9999"},
        {"HTTPS": "HTTPS://120.83.106.143:9999"},
        {"HTTPS": "HTTPS://182.35.86.229:9999"},
        {"HTTP": "HTTP://58.253.159.150:9999"},
        {"HTTP": "HTTP://123.8.125.85:9999"},
        {"HTTPS": "HTTPS://182.35.85.161:9999"},
        {"HTTPS": "HTTPS://112.85.148.32:9999"},
        {"HTTPS": "HTTPS://60.13.42.113:9999"},
        {"HTTP": "HTTP://60.13.42.24:9999"},
        {"HTTP": "HTTP://60.13.42.147:9999"},
        {"HTTP": "HTTP://60.13.42.14:9999"},
        {"HTTPS": "HTTPS://113.121.23.12:9999"},
        {"HTTPS": "HTTPS://120.83.105.126:9999"},
        {"HTTPS": "HTTPS://120.83.102.122:9999"},
        {"HTTPS": "HTTPS://117.64.251.14:808"},
        {"HTTPS": "HTTPS://117.64.148.59:808"},
        {"HTTPS": "HTTPS://117.64.148.18:808"},
        {"HTTPS": "HTTPS://117.64.251.234:808"},
        {"HTTPS": "HTTPS://117.64.250.235:808"},
        {"HTTPS": "HTTPS://117.64.250.12:808"},
        {"HTTP": "HTTP://60.13.42.47:9999"},
        {"HTTP": "HTTP://163.204.245.61:9999"},
        {"HTTPS": "HTTPS://163.204.240.252:9999"},
        {"HTTP": "HTTP://163.204.240.80:9999"},
        {"HTTP": "HTTP://123.163.122.53:9999"},
        {"HTTP": "HTTP://113.65.5.238:8118"},
        {"HTTP": "HTTP://123.8.122.114:9999"},
        {"HTTPS": "HTTPS://183.166.21.91:9999"},
        {"HTTPS": "HTTPS://113.110.46.62:9999"},
        {"HTTPS": "HTTPS://175.43.142.136:9999"},
        {"HTTP": "HTTP://163.204.245.7:9999"},
        {"HTTP": "HTTP://120.83.111.213:9999"},
        {"HTTPS": "HTTPS://163.204.242.202:9999"},
        {"HTTPS": "HTTPS://163.204.244.165:9999"},
        {"HTTP": "HTTP://163.204.246.103:9999"},
        {"HTTP": "HTTP://61.176.223.7:58822"},
        {"HTTPS": "HTTPS://123.52.43.64:8118"},
        {"HTTPS": "HTTPS://112.85.171.49:9999"},
        {"HTTPS": "HTTPS://113.117.195.24:9999"},
    ]
    # MongoDB设置
    client = pymongo.MongoClient("127.0.0.1", 27017)
    db = client['dangdang']
    coll = db[key]
    thread_list = []
    for i in range(1, 20):
        t = threading.Thread(target=get_data, args=(key, i, header, ip_proxies, coll))
        t.start()
        thread_list.append(t)
    for th in thread_list:
        th.join()


