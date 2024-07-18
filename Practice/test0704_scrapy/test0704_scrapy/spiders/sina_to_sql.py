import scrapy
from test0704_scrapy.items import Test0704ScrapyItem


class SinaToSqlSpider(scrapy.Spider):
    name = "sina_to_sql"
    allowed_domains = ["sina.com.cn"]
    start_urls = ["https://sina.com.cn"]

    def parse(self, response, **kwargs):
        items = Test0704ScrapyItem()
        items['key_titles'] = response.xpath('//title/text()').extract()
        items['key_words'] = response.xpath("//meta[@name='description']/@content").extract()
        print(items)
        yield items
        pass
