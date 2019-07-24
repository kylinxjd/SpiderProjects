# -*- coding: utf-8 -*-
import scrapy

from my_spider.items import MySpiderItem


class JobspiderSpider(scrapy.Spider):
    name = 'jobspider'
    allowed_domains = ['www.job5156.com/s/result/kt0_kw-python/']
    start_urls = ['http://www.job5156.com/s/result/kt0_kw-python/']

    def parse(self, response):
        """
        解析url返回的响应对象
        匹配下一次要访问的路径
        提取item
        :param response:
        :return:
        """
        print("#####################")
        # print(response)

        position_node_list = response.xpath('//ul[@class="position_content"]/li')
        items = []

        for position_node in position_node_list:
            # 获取详细信息
            position = position_node.xpath('./div/div[2]/div/p/a/@title').extract()
            position_url = position_node.xpath('./div/div[2]/div/p/a/@href').extract()
            salary = position_node.xpath('./div/div[2]/div/span/text()').extract()
            company = position_node.xpath('./div/div[2]/a[@class="com_name"]/@title').extract()
            require = position_node.xpath('./div/div[3]/div/text()').extract()
            # 主要业务
            professional_work = position_node.xpath('./div/div[3]/p/span/text()').extract()
            update_time = position_node.xpath('./div/div[4]/p/span/text()').extract()
            welfare_node = position_node.xpath('./div/div[4]/div')

            welfare = welfare_node[0].xpath('./span/text()').extract()

            # 实例化MySpiderItem()对象
            item = MySpiderItem()
            item['position'] = position[0]
            item['position_url'] = position_url[0]
            item['salary'] = salary[0]
            item['company'] = company[0]
            item['require'] = require[0].strip().replace(' ', '').replace('\r\n', '')
            item['professional_work'] = professional_work[0]
            item['update_time'] = update_time[0]
            item['welfare'] = welfare
            items.append(item)

        # 抛出items，保存到csv
        return items

    def second_handler(self):
        pass
