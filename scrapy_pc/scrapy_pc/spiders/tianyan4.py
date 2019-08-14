# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class Tianyan4Spider(CrawlSpider):
    name = 'tianyan4'
    allowed_domains = ['www.skeyedu.com']
    start_urls = ['http://www.skeyedu.com/']
    # 决定当前的爬虫的爬取规则
    rules = (
        # Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    )
    """
    allow()填写正则规则，符合正则的url将会被提取，如果不写，默认提取全部
    deny()满足括号里的正则一律不提取，优先级高于allow()
    """

    def parse_item(self, response):
        item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        return item
