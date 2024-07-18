# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import json
import os
from datetime import datetime

class QiqiharPipeline:

    def __init__(self):
        output_dir = '/Users/fanjindong/Desktop/Semester-3/Submission/main/weather_data_collections/Collection_of_Spider/cn'
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        self.daily_file_path = os.path.join(output_dir, f"qiqihar_weather_daily_{timestamp}.jsonl")
        self.hourly_file_path = os.path.join(output_dir, f"qiqihar_weather_hourly_{timestamp}.jsonl")
        self.daily_file = None
        self.hourly_file = None

    def open_spider(self, spider):
        self.daily_file = open(self.daily_file_path, 'w', encoding='utf-8')
        self.hourly_file = open(self.hourly_file_path, 'w', encoding='utf-8')

    def close_spider(self, spider):
        self.daily_file.close()
        self.hourly_file.close()

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        if 'time' in item:
            self.hourly_file.write(line)
        else:
            self.daily_file.write(line)
        return item