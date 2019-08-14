# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class Scrapy25Spider(CrawlSpider):
    name = 'scrapy25'
    allowed_domains = ['news.ifeng.com/']
    start_urls = ['http://news.ifeng.com//']

    rules = (
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = {}
        # item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        # item['name'] = response.xpath('//div[@id="name"]').get()
        # item['description'] = response.xpath('//div[@id="description"]').get()
        node_list = response.xpath(
            '//ul[@class="news-stream-basic-news-list"]/li[@class="news-stream-newsStream-news-item-has-image clearfix news_item"]')
        for node in node_list:
            title = node.xpath('./a[1]/@title').extract_first()
            detail_url = node.xpath('./a[1]/@href').extract_first()
            yield scrapy.Request(url=detail_url, callback=self.detail_parse, meta={'title': title})

    def detail_parse(self, response):
        title = response.meta['title']
        print("SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS")
        print(title)
        pass
