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
        # 列表推导式生成url列表
        self.url_list = [self.base_url % (i * 25) for i in range(10)]

    def send_request(self, url):
        res = requests.get(url, headers=self.headers)
        html = res.text
        return self.responses_handler(html)

    def responses_handler(self, html_str):
        html_doc = etree.HTML(html_str)

        movie_name = html_doc.xpath('//ol/li/div/div[2]/div[1]/a/span[1]/text()')
        movie_score = html_doc.xpath('//ol/li[1]/div/div[2]/div[2]/div/span[2]/text()')
        self.data_queue.put(movie_name + movie_score)

    def start_work(self):
        thread_list = []
        for url in self.url_list:
            thread_obj = threading.Thread(target=self.send_request, args=(url,))
            thread_obj.start()
            thread_list.append(thread_obj)

        for thread in thread_list:
            thread.join()


if __name__ == '__main__':
    douban = Douban()
    douban.start_work()
