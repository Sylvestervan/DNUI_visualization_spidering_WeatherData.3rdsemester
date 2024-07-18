# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Test0702ScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url_name = scrapy.Field()
    url_text = scrapy.Field()
    pass
