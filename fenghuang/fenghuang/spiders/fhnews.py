# -*- coding: utf-8 -*-
import re

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class FhnewsSpider(CrawlSpider):
    name = 'fhnews'
    allowed_domains = ['news.ifeng.com']
    start_urls = ['http://news.ifeng.com/']

    rules = (
        # Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'^http://news.ifeng.com/$'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        # item = {}
        node_list = response.xpath(
            '//ul[@class="news-stream-basic-news-list"]/li[@class="news-stream-newsStream-news-item-has-image clearfix news_item"]')
        print(":" * 30)
        print(len(node_list))
        for node in node_list:
            title = node.xpath('./a[1]/@title').extract_first()
            detail_url = "http:" + node.xpath('./a[1]/@href').extract_first()
            print(":::::::::::::::::::::", title)
            print(":::::::::::::::::::::", detail_url)
            # yield scrapy.Request(url=detail_url, callback=self.detail_parse, meta={'title': title}, dont_filter=True)
            # break
        # return item

    def detail_parse(self, response):

        item = {}

        item['title'] = response.meta['title']

        item['time'] = response.xpath('//*[@id="root"]/div/div[3]/div[1]/div[1]/div[1]/div[1]/p/span[1]/text()').extract_first()

        item['origin'] = response.xpath('//*[@id="root"]/div/div[3]/div[1]/div[1]/div[1]/div[1]/p/span[3]/span/a/text()').extract_first()

        content = response.xpath('//div[@class="text-3zQ3cZD4"]/p/text()').extract()

        content2 = ''.join(content)

        item['content'] = re.sub(r'\s', '', content2)

        print(item)
