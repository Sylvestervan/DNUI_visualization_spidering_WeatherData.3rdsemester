import scrapy
from test0703_scrapy.items import Test0703ScrapyItem

class TitleTextSpider(scrapy.Spider):
    name = "title_text"
    allowed_domains = ["sina.com.cn"]
    start_urls = ["https://sina.com.cn"]

    def parse(self, response, **kwargs):
        items = Test0703ScrapyItem()
        items['Title'] = response.xpath('//title/text()').extract()
        yield items
