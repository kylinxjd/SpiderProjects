# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from baidufinance.items import BaidufinanceItem


class BaiducrawlSpider(CrawlSpider):
    name = 'baiducrawl'
    allowed_domains = ['news.baidu.com']
    start_urls = ['http://news.baidu.com/finance']

    rules = (
        # Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'http://news.baidu.com/finance'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = {}
        # item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        # item['name'] = response.xpath('//div[@id="name"]').get()
        # item['description'] = response.xpath('//div[@id="description"]').get()
        node_list = response.xpath('//ul[@class="ulist fb-list"]/li')
        print(len(node_list))
        for node in node_list:
            title = node.xpath('./a/text()').extract_first()
            detail_url = node.xpath('./a/@href').extract_first()
            print(":::::::::::::::::::::", title)
            print(":::::::::::::::::::::", detail_url)
            yield scrapy.Request(url=detail_url, callback=self.detail_parse, meta={'title': title, 'url': detail_url},
                                 dont_filter=True)
        # return item

    def detail_parse(self, response):

        author = response.xpath('//div[@class="author-txt"]/p[@class="author-name"]/text()').extract()[0]
        publish_time1 = response.xpath('//div[@class="author-txt"]/div/span[1]/text()').extract()[0]
        publish_time2 = response.xpath('//div[@class="author-txt"]/div/span[2]/text()').extract()[0]
        publish_time = publish_time1 + ' ' + publish_time2

        content_list = response.xpath('//div[@class="article-content"]/p/span/text()').extract()
        content = ''.join(content_list)

        item = BaidufinanceItem()

        item['title'] = response.meta['title']
        item['url'] = response.meta['url']
        item['author'] = author
        item['publish_time'] = publish_time
        item['content'] = content

        yield item
