# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql

#TODO Practice Project --- Part 4
class Test0704ScrapyPipeline:
    def __init__(self):
        self.conn = pymysql.connect(
            host='localhost',
            user='root',
            password='fjd2023dnui',
            database='test_project_part_4'
        )
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        key_titles = item['key_titles'][0]
        key_words = item['key_words'][0]
        print(key_titles, key_words)
        sql_by_sina = "insert into news_info(key_titles, key_words) values ('"+key_titles+"', '"+key_words+"')"
        self.cursor.execute(sql_by_sina)
        self.conn.commit()
        return item

    def shut_down_spider(self, spider):
        self.conn.close()