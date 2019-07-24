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

    for p in range(page, page + 1):

        print("第%s页-----------------" % p)

        url = 'http://search.dangdang.com/?key=%s&act=input&page_index=%s' % (key, page)
        # 获取一级页面
        try:
            res = requests.get(url=url, headers=head, proxies=proxy[random.randint(0, 18)])
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
            # 获取二级页面详情
            try:
                res2 = requests.get(url=detail_url, headers=head, proxies=proxy[random.randint(0, 18)])
            except Exception as e:
                print(e)
                continue
            detail_html = res2.text
            sleep(random.randint(0, 180) / 1000)
            soup2 = BeautifulSoup(detail_html, 'html.parser')

            obj1 = soup2.select('div[class="sale_box_left"] div[class="name_info"] h1')
            author_obj = soup2.select('div[class="messbox_info"] span a[dd_name="作者"]')
            publish_house_obj = soup2.select('div[class="messbox_info"] span a[dd_name="出版社"]')
            publish_time_obj = soup2.select('div[class="messbox_info"] span')
            price_obj = soup2.select('p[id="dd-price"]')
            isbn_obj = soup2.select('ul[class="key clearfix"] li')
            try:
                # 书名
                if not obj1:
                    continue
                bookname = obj1[0].attrs['title']
                # 作者
                if not author_obj:
                    author = '---'
                elif len(author_obj) > 1:
                    # 外国作者
                    author = ''
                    for auth in author_obj[:-1]:
                        author += auth.get_text() + ' '
                    author += '(' + author_obj[-1].get_text() + ')'
                else:
                    # 中国作者
                    author = author_obj[0].get_text()
                # 出版社
                if not publish_house_obj:
                    publish = '---'
                else:
                    publish = publish_house_obj[0].get_text()
                # 出版时间
                if len(publish_time_obj) > 2:
                    publish_time = publish_time_obj[2].get_text().strip().split(':')[1]
                else:
                    publish_time = '---'

                # 价格
                price = price_obj[0].get_text().split('¥')[1]

                # isbn
                isbn = ''
                for isb in isbn_obj:
                    if "国际标准书号ISBN" == isb.get_text().strip().split('：')[0]:
                        isbn = isb.get_text().strip().split('：')[1]
                        break
                if not isbn:
                    isbn = "---"

                data = {
                    "book_name": bookname,
                    "author": author,
                    "publish": publish,
                    "publish_time": publish_time,
                    "price": price.strip(),
                    "ISBN": isbn
                }
                print(data['book_name'])
                data_list.append(data)
            except Exception as e:
                print(e)
                continue

        coll.insert(data_list)


if __name__ == '__main__':
    key = 'C'
    header = {
        'Pragma': 'no-cache',
        'Referer': 'http://search.dangdang.com/?key=%s&act=input' % key,
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
        'Cookie': 'from=P-295132-217563_64_0__1; order_follow_source=P-295132-2%7C%231%7C%23c.duomai.com%252Ftrack.php%253Fsite_id%253D217563%2526aid%253D64%2526euid%253D%2526t%253Dhttp%25253a%25252f%25252fwww.dangdang.com%25252f%7C%230%7C%233BlvQv02FQCb-%7C-; ddscreen=2; __permanent_id=20190720154036144174983416090664471; __visit_id=20190720154036146845894385985963627; __out_refer=1563608436%7C!%7Cc.duomai.com%7C!%7C; __ddc_1d=1563608436%7C!%7C_ddclickunion%3DP-295132-217563_64_0__1; __ddc_24h=1563608436%7C!%7C_ddclickunion%3DP-295132-217563_64_0__1; __ddc_15d=1563608436%7C!%7C_ddclickunion%3DP-295132-217563_64_0__1; __ddc_15d_f=1563608436%7C!%7C_ddclickunion%3DP-295132-217563_64_0__1; __rpm=%7Cmix_317715...1563608443674; search_passback=91da83bf7b229c4f7fc5325d00000000; __trace_id=20190720154047317168208131370294392; dest_area=country_id%3D9000%26province_id%3D111%26city_id%3D0%26district_id%3D0%26town_id%3D0; pos_9_end=1563608447466; pos_0_end=1563608447563; pos_0_start=1563608448650'
    }
    ip_proxies = [
        {'HTTPS': 'HTTPS://113.124.86.206:9999'},
        {'HTTPS': 'HTTPS://42.238.82.163:9999'},
        {'HTTPS': 'HTTPS://120.83.109.74:9999'},
        {'HTTPS': 'HTTPS://58.56.149.198:53281'},
        {'HTTP': 'HTTP://182.34.27.68:9999'},
        {'HTTP': 'HTTP://163.204.93.220:9999'},
        {'HTTP': 'HTTP://171.15.172.171:9999'},
        {'HTTP': 'HTTP://112.111.217.188:9999'},
        {'HTTP': 'HTTP://171.15.51.60:9999'},
        {'HTTP': 'HTTP://42.238.90.107:9999'},
        {'HTTP': 'HTTP://218.73.118.18:9999'},
        {'HTTP': 'HTTP://182.34.27.226:9999'},
        {'HTTP': 'HTTP://171.15.65.187:9999'},
        {'HTTP': 'HTTP://42.238.80.233:9999'},
        {'HTTPS': 'HTTPS://111.226.211.74:8118'},
        {'HTTPS': 'HTTPS://113.120.39.173:9999'},
        {'HTTPS': 'HTTPS://113.117.66.225:9999'},
        {'HTTPS': 'HTTPS://49.70.18.190:61234'},
        {'HTTP': 'HTTP://42.238.91.63:9999'},
        {"http": "http://61.135.155.82:443"}
    ]
    client = pymongo.MongoClient("127.0.0.1", 27017)
    db = client['dangdang']
    coll = db['计算机']
    for i in range(20, 29):
        t = threading.Thread(target=get_data, args=(key, i * 1 + 1, header, ip_proxies, coll))
        t.start()

