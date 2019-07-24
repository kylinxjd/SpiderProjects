from time import sleep

import pymongo
import random
import re
import threading
from queue import Queue

import requests
from lxml import etree


class SuNing(object):

    def __init__(self):

        self.client = pymongo.MongoClient("127.0.0.1", 27017)
        self.db = self.client['spider']
        self.coll = self.db['suning']

        self.base_url = 'https://list.suning.com/emall/searchV1Product.do'

        self.data_queue = Queue()

        self.cookie = 'tradeMA=38; _snsr=direct%7Cdirect%7C%7C%7C; _snvd=1563775822712eoxm5Btl+Wk; cityCode=010; districtId=10106; SN_CITY=10_010_1000000_9017_01_10106_4_0; cityId=9017; _snzwt=THZA3W16c184d69d2fQNabc5c; hm_guid=4376c320-6f41-499d-a619-194b62cd3f10; _df_ud=21e6d31f-ac38-428e-b7a3-da2fecd31808; _device_session_id=p_52831963-e1f5-4204-9ee6-c0f748c438de; _cp_dt=7ea4bee8-7b8b-4050-a533-9c493ff70250-00029; _snms=156377771410823178; smhst=10638755882|0000000000a10985347748|0070094634a10597918588|0000000000a10597840415|0000000000; authId=si3A5018CD1C15041FF855291062773333; secureToken=A54AD6CE39D7D03F1BF9CD5FACFCAE91; _snma=1%7C156377582108573987%7C1563775821085%7C1563782890497%7C1563784218817%7C29%7C2; _snmp=156378421716294198; _snmb=15637810680674001%7C1563784218909%7C1563784218838%7C9'

        self.url_list = []

        for i in range(10, 18):  # 大页
            for j in range(1, 4):  # 每大页的三小页
                self.url_list.append(self.base_url + '?ci=20006&pg=03&cp=' + str(i)
                                     + '&il=0&iy=-1&hf=brand_Name_FacetAll:%E5%8D%8E%E4%B8%BA%28HUAWEI%29&isNoResult=0&n=1&sesab=&id=IDENTIFYING&cc=010&paging=' + str(
                    j) + '&sub=1&jzq=2166')

        self.user_agents = [
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
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"
        ]
        self.proxies = [
            {"HTTPS": "HTTPS://119.176.194.30:9999"},
            {"HTTP": "HTTP://171.11.178.239:9999"},
            {"HTTP": "HTTP://121.233.206.165:9999"},
            {"HTTP": "HTTP://1.198.72.49:9999"},
            {"HTTP": "HTTP://1.198.108.250:9999"},
            {"HTTPS": "HTTPS://218.91.112.183:9999"},
            {"HTTP": "HTTP://171.80.2.223:9999"},
            {"HTTPS": "HTTPS://114.230.69.10:9999"},
            {"HTTP": "HTTP://121.233.207.77:9999"},
            {"HTTP": "HTTP://117.85.160.61:8118"},
            {"HTTPS": "HTTPS://171.11.33.142:9999"},
            {"HTTPS": "HTTPS://123.163.96.238:9999"},
            {"HTTP": "HTTP://1.198.73.36:9999"},
            {"HTTP": "HTTP://123.169.39.179:9999"},
            {"HTTP": "HTTP://121.233.206.203:9999"},
            {"HTTP": "HTTP://171.12.113.33:9999"},
            {"HTTP": "HTTP://113.124.94.0:9999"},
            {"HTTP": "HTTP://42.238.90.250:9999"},
            {"HTTP": "HTTP://222.189.191.95:9999"},
            {"HTTP": "HTTP://59.32.37.198:3128"},
            {"HTTP": "HTTP://113.121.23.37:9999"},
            {"HTTP": "HTTP://116.208.53.37:9999"},
            {"HTTPS": "HTTPS://114.230.86.129:9999"},
            {"HTTP": "HTTP://123.169.37.30:9999"},
            {"HTTP": "HTTP://117.91.131.104:9999"},
            {"HTTP": "HTTP://1.197.204.184:9999"},
            {"HTTP": "HTTP://222.89.32.173:9999"},
            {"HTTP": "HTTP://123.163.97.250:9999"},
            {"HTTP": "HTTP://58.253.156.201:9999"},
            {"HTTP": "HTTP://222.189.190.146:9999"},
            {"HTTPS": "HTTPS://113.128.26.57:9999"},
            {"HTTP": "HTTP://1.197.203.44:9999"},
            {"HTTPS": "HTTPS://120.83.104.108:9999"},
            {"HTTP": "HTTP://1.197.203.46:9999"},
            {"HTTPS": "HTTPS://171.12.112.213:9999"},
            {"HTTP": "HTTP://58.253.154.136:9999"},
            {"HTTP": "HTTP://1.197.204.52:9999"},
            {"HTTP": "HTTP://175.44.109.206:9999"},
            {"HTTPS": "HTTPS://222.189.190.117:9999"},
            {"HTTP": "HTTP://123.8.115.221:9999"},
            {"HTTPS": "HTTPS://182.34.27.0:9999"},
            {"HTTP": "HTTP://171.80.0.131:9999"},
            {"HTTP": "HTTP://182.116.234.232:9999"},
            {"HTTPS": "HTTPS://171.80.2.165:9999"},
            {"HTTP": "HTTP://112.85.166.226:9999"},
            {"HTTP": "HTTP://27.43.186.247:9999"},
            {"HTTP": "HTTP://171.80.0.82:9999"},
            {"HTTPS": "HTTPS://122.137.173.19:8080"},
            {"HTTP": "HTTP://113.128.8.9:9999"},
            {"HTTP": "HTTP://117.91.130.41:9999"},
            {"HTTP": "HTTP://58.253.156.50:9999"},
            {"HTTP": "HTTP://121.233.251.90:9999"},
            {"HTTP": "HTTP://163.204.93.26:9999"},
            {"HTTPS": "HTTPS://116.208.54.133:9999"},
            {"HTTPS": "HTTPS://116.208.11.19:9999"},
            {"HTTPS": "HTTPS://1.198.73.123:9999"},
            {"HTTPS": "HTTPS://119.33.64.3:8118"},
            {"HTTPS": "HTTPS://222.189.144.69:9999"},
            {"HTTP": "HTTP://58.253.155.223:9999"},
            {"HTTP": "HTTP://125.109.196.71:61234"},
            {"HTTP": "HTTP://114.230.24.4:9999"},
            {"HTTP": "HTTP://182.34.37.91:9999"},
            {"HTTP": "HTTP://121.233.251.95:9999"},
            {"HTTPS": "HTTPS://116.208.52.147:9999"},
            {"HTTPS": "HTTPS://180.119.68.48:9999"},
            {"HTTP": "HTTP://144.255.49.63:9999"},
            {"HTTP": "HTTP://121.233.251.98:9999"},
            {"HTTPS": "HTTPS://42.238.88.73:9999"},
            {"HTTPS": "HTTPS://116.208.11.13:9999"},
            {"HTTPS": "HTTPS://124.93.201.59:59618"},
            {"HTTP": "HTTP://111.177.106.57:9999"},
            {"HTTP": "HTTP://123.8.121.138:9999"},
            {"HTTP": "HTTP://222.189.144.215:9999"},
            {"HTTP": "HTTP://119.130.107.153:3128"},
            {"HTTPS": "HTTPS://58.253.152.196:9999"},
            {"HTTP": "HTTP://123.169.35.148:9999"},
            {"HTTP": "HTTP://120.83.106.123:9999"},
            {"HTTP": "HTTP://111.177.106.169:9999"},
            {"HTTPS": "HTTPS://180.107.179.44:8118"},
            {"HTTP": "HTTP://180.119.141.141:9999"},
            {"HTTPS": "HTTPS://123.169.35.55:9999"},
            {"HTTPS": "HTTPS://116.208.11.248:9999"},
            {"HTTP": "HTTP://115.53.22.245:9999"},
            {"HTTP": "HTTP://171.13.102.142:9999"},
            {"HTTP": "HTTP://163.204.246.117:9999"},
            {"HTTPS": "HTTPS://110.189.152.86:52277"},
            {"HTTPS": "HTTPS://60.190.250.120:8080"},
            {"HTTPS": "HTTPS://115.219.105.102:8010"},
            {"HTTP": "HTTP://121.61.25.201:61234"},
            {"HTTPS": "HTTPS://113.128.29.232:9999"},
            {"HTTPS": "HTTPS://113.128.10.82:9999"},
            {"HTTPS": "HTTPS://113.128.24.25:9999"},
            {"HTTPS": "HTTPS://113.128.27.82:9999"},
            {"HTTPS": "HTTPS://113.117.116.43:9999"},
            {"HTTP": "HTTP://175.175.216.116:1133"},
            {"HTTPS": "HTTPS://222.128.9.235:59593"},
            {"HTTPS": "HTTPS://119.254.94.93:46323"},
            {"HTTPS": "HTTPS://182.35.81.59:9999"},
            {"HTTPS": "HTTPS://182.35.81.201:9999"},
            {"HTTPS": "HTTPS://182.35.84.241:9999"}
        ]

    def send_request(self, url):
        # try:
        ret = requests.get(url=url, headers={
            'cookie': self.cookie,
            'pragma': 'no-cache',
            'referer': 'https://list.suning.com/0-20006-0-0-0-0-0-0-0-0-11635.html?safp=d488778a.phone2018.103327226421.5',
            'user-agent': self.user_agents[random.randint(0, 16)],
            'x-requested-with': 'XMLHttpRequest'
        }, proxies=self.proxies[random.randint(0, 96)])
        html = ret.text
        self.response_handler(html)
        # except Exception as e:
        #     print(e)
        #     print("ssssssssssssss")

    def response_handler(self, html_str):
        """
        处理返回的html文档
        :param html_str:
        :return:
        """
        html_doc = etree.HTML(text=html_str)
        # 获取二级页面路径
        detail_url_list = html_doc.xpath('//li/div/div/div[2]/div[2]/a/@href')
        data_list = []
        for detail_url in detail_url_list:
            # 获取二级页面详情
            detail_res = requests.get(url="https:" + detail_url,
                                      headers={'user-agent': self.user_agents[random.randint(0, 16)]},
                                      proxies=self.proxies[random.randint(0, 96)])
            detail_html = detail_res.text
            detail_html_doc = etree.HTML(detail_html)

            # 获取详细信息
            title = detail_html_doc.xpath('//div[@class="proinfo-title"]/h1/text()')
            second_title = detail_html_doc.xpath('//div[@class="proinfo-title"]/h2/text()')
            system_version = detail_html_doc.xpath(
                '//div[@class="procon-param"]/table[2]/tbody/tr[@parametercode="001686"]/td[2]/text()')
            back_camera = detail_html_doc.xpath(
                '//div[@class="procon-param"]/table[2]/tbody/tr[@parametercode="012057"]/td[2]/text()')
            screen_size = detail_html_doc.xpath(
                '//div[@class="procon-param"]/table[2]/tbody/tr[@parametercode="010025"]/td[2]/text()')
            screen_material = detail_html_doc.xpath(
                '//div[@class="procon-param"]/table[2]/tbody/tr[@parametercode="011486"]/td[2]/text()')
            screen_resolution = detail_html_doc.xpath(
                '//div[@class="procon-param"]/table[2]/tbody/tr[@parametercode="014834"]/td[2]/text()')
            color = detail_html_doc.xpath(
                '//div[@class="procon-param"]/table[2]/tbody/tr[@parametercode="009715"]/td[2]/text()')
            cpu = detail_html_doc.xpath(
                '//div[@class="procon-param"]/table[2]/tbody/tr[@parametercode="000020"]/td[2]/text()')
            ram = detail_html_doc.xpath(
                '//div[@class="procon-param"]/table[2]/tbody/tr[@parametercode="009130"]/td[2]/text()')
            storage = detail_html_doc.xpath(
                '//div[@class="procon-param"]/table[2]/tbody/tr[@parametercode="010664"]/td[2]/text()')
            battery = detail_html_doc.xpath(
                '//div[@class="procon-param"]/table[2]/tbody/tr[@parametercode="006788"]/td[2]/text()')
            model = detail_html_doc.xpath(
                '//div[@class="procon-param"]/table[2]/tbody/tr[@parametercode="001360"]/td[2]/text()')
            market_time = detail_html_doc.xpath(
                '//div[@class="procon-param"]/table[2]/tbody/tr[@parametercode="001012"]/td[2]/text()')

            # 获取价格地址
            key1 = detail_url.split('/')[-1].split('.')[0].zfill(18)
            key2 = detail_url.split('/')[-2].zfill(10)
            # https://pas.suning.com/nspcsale_0_000000010638755882_000000010638755882_0000000000_10_010_0100101.html?callback=pcData&_=4387676
            base_price_url = 'https://pas.suning.com/nspcsale_0_%s_%s_%s_10_010_0100101.html?callback=pcData&_=4387676'
            price_url = base_price_url % (key1, key1, key2)
            res = requests.get(url=price_url, headers={'user-agent': self.user_agents[random.randint(0, 16)]},
                               proxies=self.proxies[random.randint(0, 96)])
            price_text = res.text
            # 获取价格
            try:
                price = re.findall(r'"promotionPrice":"(.*?)"', price_text)[0]
            except:
                price = '---'
            try:
                data = {
                    'title': title[0],
                    'second_title': second_title[0],
                    'system_version': system_version[0] if system_version else "---",
                    'back_camera': back_camera[0] if back_camera else "---",
                    'screen_material': screen_material[0] if screen_material else "---",
                    'screen_size': screen_size[0],
                    'screen_resolution': screen_resolution[0] if screen_resolution else "---",
                    'color': color[0] if color else "---",
                    'cpu': cpu[0],
                    'ram': ram[0],
                    'storage': storage[0],
                    'battery': battery[0] if battery else "---",
                    'model': model[0],
                    'market_time': market_time[0],
                    'price': ''.join(price)
                }
            except Exception as e:
                print(e)
            else:
                print(data['model'])
                data_list.append(data)
            sleep(random.randint(20, 400) / 1000)
        self.coll.insert(data_list)

    def start_work(self):
        thread_list = []
        for url in self.url_list:
            thread_obj = threading.Thread(target=self.send_request, args=(url,))
            thread_obj.start()
            thread_list.append(thread_obj)

        for thread in thread_list:
            thread.join()

        # while not self.data_queue.empty():
        #     print(self.data_queue.get())


if __name__ == '__main__':
    suning = SuNing()
    # print(suning.url_list)
    # suning.send_request(suning.url_list[0])
    suning.start_work()
