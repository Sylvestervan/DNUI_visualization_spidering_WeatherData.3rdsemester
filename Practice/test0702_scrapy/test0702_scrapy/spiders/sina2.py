import scrapy
from test0702_scrapy.items import Test0702ScrapyItem

class Sina(scrapy.Spider):
    name = 'sina2'
    allowed_domains = ['sina.com.cn', 'jd.com']
    start_urls = ("https://sports.sina.com.cn/global/europe/2024-07-01/doc-incaqvnq3209143.shtml",
                  "https://sports.sina.com.cn/china/2024-07-01/doc-incaqvnq3231242.shtml",
                  "https://sports.sina.com.cn/g/pl/2024-07-01/doc-incaqvnq3203595.shtml",
                  "https://sports.sina.com.cn/g/pl/2024-07-02/doc-incasymq2390182.shtml")

    url2 = (
        'https://www.jd.com/',
        'https://www.sina.com.cn/'
    )

    def start_requests(self):
        for url in self.url2:
            yield scrapy.Request(url, self.parse)

    def parse(self, response, **kwargs):
        item = Test0702ScrapyItem()
        item['url_text'] = response.xpath('//title/text()').get()    # 使用xpath表达式对响应中的数据进行提取
        print(f"URL: {response.url}, Title: {item['url_text']}")
        yield item

