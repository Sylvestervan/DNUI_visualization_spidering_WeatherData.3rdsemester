# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import codecs

class Test0703ScrapyPipeline(object):
    def __init__(self):
        self.file = codecs.open('/Users/fanjindong/Desktop/Semester-3/Practice/test_02.txt', 'wb', encoding='utf-8')

    def process_item(self, item, spider):
        info = str(item) + '\n'
        print(info)
        self.file.write(info)
        return item

    def shut_down_spider(self, spider):
        self.file.close()
