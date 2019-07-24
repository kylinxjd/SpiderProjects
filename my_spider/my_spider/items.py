# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MySpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # 岗位名称
    position = scrapy.Field()
    # 职位网址
    position_url = scrapy.Field()
    # 薪水
    salary = scrapy.Field()
    # 公司名称
    company = scrapy.Field()
    # 公司主营业务
    professional_work = scrapy.Field()
    # 更新时间
    update_time = scrapy.Field()
    # 公司福利
    welfare = scrapy.Field()
    # 招聘要求
    require = scrapy.Field()

