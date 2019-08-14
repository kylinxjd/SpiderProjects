# -*- coding: utf-8 -*-
import scrapy


class TestipSpider(scrapy.Spider):
    name = 'testip'
    allowed_domains = []

    def start_requests(self):
        url = 'http://www.baidu.com/'

        for i in range(4):
            yield scrapy.Request(url=url, callback=self.parse, dont_filter=True)

    def parse(self, response):
        print(response.text)
