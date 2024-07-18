import scrapy
from test0702_scrapy.items import Test0702ScrapyItem

class SinascrapySpider(scrapy.Spider):
    name = "sinascrapy"
    allowed_domains = ["sina.com.cn"]
    start_urls = ("https://sports.sina.com.cn/global/europe/2024-07-01/doc-incaqvnq3209143.shtml",
                  "https://sports.sina.com.cn/china/2024-07-01/doc-incaqvnq3231242.shtml",
                  "https://sports.sina.com.cn/g/pl/2024-07-01/doc-incaqvnq3203595.shtml",
                  "https://sports.sina.com.cn/g/pl/2024-07-02/doc-incasymq2390182.shtml")

    def parse(self, response, **kwargs):
        item = Test0702ScrapyItem()
        item['url_name'] = response.xpath('//*[contains(concat(" ", @class, " "), concat(" ", "main-title", " "))]/text()').get()
        print(item['url_name'])
        yield item
        pass