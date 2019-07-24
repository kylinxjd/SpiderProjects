# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import csv

from scrapy.exceptions import DropItem

from baidufinance.items import BaidufinanceItem


class BaidufinancePipeline(object):
    def __init__(self):
        self.urls = set()

    def process_item(self, item, spider):

        if isinstance(item, BaidufinanceItem):

            if item['url'] in self.urls:
                raise DropItem("Duplicate item found: %s" % item)
            else:
                self.urls.add(item['url'])
                with open('baidu.csv', 'a+', newline='') as f:
                    w = csv.writer(f)
                    w.writerow(dict(item).values())

            return item
