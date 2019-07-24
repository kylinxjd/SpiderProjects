# -*- coding: utf-8 -*-
import scrapy

from baidufinance.items import BaidufinanceItem


class FinanceSpider(scrapy.Spider):
    name = 'finance'
    allowed_domains = ['news.baidu.com/finance']
    start_urls = ['http://news.baidu.com/finance/']

    def parse(self, response):
        node_list = response.xpath('//ul[@class="ulist fb-list"]/li')[1:]
        # print("sssssssssssssssssssssssss")
        # print(len(node_list))
        for node in node_list:
            title = node.xpath('./a/text()').extract()[0]
            url = node.xpath('./a/@href').extract()[0]
            yield scrapy.Request(url=url,
                                 callback=self.second_handler,
                                 meta={'title': title, 'url': url},
                                 dont_filter = True)



    def second_handler(self, response):
        print("dddddddddddddddddddddddddd")

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

        print(item)

        yield item
