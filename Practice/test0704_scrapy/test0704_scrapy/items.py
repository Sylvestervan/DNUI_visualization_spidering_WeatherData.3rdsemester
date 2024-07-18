# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Test0704ScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    key_titles = scrapy.Field()
    key_words = scrapy.Field()
    pass
