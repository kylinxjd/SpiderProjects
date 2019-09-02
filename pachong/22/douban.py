import threading
from queue import Queue

import requests
from lxml import etree


class Douban(object):

    def __init__(self):
        self.base_url = 'https://movie.douban.com/top250?start=%s'
        self.data_queue = Queue()
        self.headers = {
            'Referer': 'https://movie.douban.com/top250',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
        }
        self.url_list = [self.base_url % (i * 25) for i in range(1)]

    def send_request(self, url):
        ret = requests.get(url=url, headers=self.headers, proxies={
            "http": "http://61.135.155.82:443"
        })
        # 获取HTML文本文档
        html = ret.text
        self.response_handler(html)

    def response_handler(self, html_str):
        """
        处理返回的html文档
        :param html_str:
        :return:
        """
        html_doc = etree.HTML(text=html_str)
        li_list = html_doc.xpath('//ol/li')
        for li in li_list:
            movie_name = li.xpath('./div/div[2]/div[1]/a/span[1]/text()')
            movie_score = li.xpath('./div/div[2]/div[2]/div/span[2]/text()')
            self.data_queue.put(movie_name + movie_score)

    def start_work(self):

        thread_list = []
        for url in self.url_list:
            thread_obj = threading.Thread(target=self.send_request, args=(url,))
            thread_obj.start()
            thread_list.append(thread_obj)

        for thread in thread_list:
            thread.join()

        while not self.data_queue.empty():
            print(self.data_queue.get())


if __name__ == '__main__':
    douban = Douban()
    douban.start_work()
