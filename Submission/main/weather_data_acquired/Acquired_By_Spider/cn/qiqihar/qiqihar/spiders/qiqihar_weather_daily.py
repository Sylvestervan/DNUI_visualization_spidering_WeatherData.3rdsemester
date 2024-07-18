import scrapy
from datetime import datetime, timedelta
import re
import random
from qiqihar.items import QiqiharWeatherDailyItem

class QiqiharWeatherDailySpider(scrapy.Spider):
    name = "qiqihar_weather_daily"
    allowed_domains = ["worldweatheronline.com"]
    start_urls = ["https://www.worldweatheronline.com/qiqihar-weather-history/heilongjiang/cn.aspx"]

    def __init__(self, start_date, end_date, *args, **kwargs):
        super(QiqiharWeatherDailySpider, self).__init__(*args, **kwargs)
        self.start_date = datetime.strptime(start_date, '%Y-%m-%d')
        self.end_date = datetime.strptime(end_date, '%Y-%m-%d')
        self.current_date = self.start_date
        # self.output_path = output_path
        # self.file = open(self.output_path, 'w', encoding='utf-8')

    # def closed(self, reason):
    #     self.file.close()

    def start_requests(self):
        yield from self.make_requests_from_date(self.current_date)

    def make_requests_from_date(self, date):
        url = 'https://www.worldweatheronline.com/qiqihar-weather-history/heilongjiang/cn.aspx'
        unique_param = random.randint(0, 1000000)
        self.log(f"Making request for date: {date.strftime('%Y-%m-%d')}")
        yield scrapy.Request(url, callback=self.parse, meta={'date': date, 'unique_param': unique_param}, dont_filter=True)

    def parse(self, response, **kwargs):
        date = response.meta['date']
        self.log(f"Parsing form for date: {date.strftime('%Y-%m-%d')}")

        form_data = {
            'ctl00$MainContentHolder$txtPastDate': date.strftime('%Y-%m-%d'),
            'ctl00$MainContentHolder$butShowPastWeather': 'Get Weather'
        }
        yield scrapy.FormRequest.from_response(
            response,
            formdata=form_data,
            formxpath='//input[@id="ctl00_MainContentHolder_butShowPastWeather"]',
            callback=self.parse_daily,
            meta={'date': date, 'unique_param': response.meta['unique_param']},
            dont_filter=True
        )

    def parse_daily(self, response):
        date = response.meta['date']
        self.log(f"Parsing daily data for date: {date.strftime('%Y-%m-%d')}")

        # 使用XPath解析所需的数据字段
        temp_range = response.xpath('//div[@class="days-collapse-temp"]/text()').get()
        max_temp, min_temp = self.parse_temp_range(temp_range)
        status = response.xpath('//div[@class="days-collapse-forecast"]/text()').get()
        moonrise = response.xpath('//div[@class="days-inform"]//div[contains(@class, "days-rise")][1]/span/text()').get()
        moonset = response.xpath('//div[@class="days-inform"]//div[contains(@class, "days-set")][1]/span/text()').get()
        sunrise = response.xpath('//div[@class="days-inform"]//div[contains(@class, "days-rise")][2]/span/text()').get()
        sunset = response.xpath('//div[@class="days-inform"]//div[contains(@class, "days-set")][2]/span/text()').get()

        items = QiqiharWeatherDailyItem(
            location='qiqihar',
            date=date.strftime('%Y-%m-%d'),
            min_temp=min_temp,
            max_temp=max_temp,
            status=status,
            moonrise=moonrise,
            moonset=moonset,
            sunrise=sunrise,
            sunset=sunset
        )

        self.log(f"Yielding data: {items}")
        yield items
        print(items)
        # self.file.write(json.dumps(items) + '\n')

        # Check if there is a next date to process
        if date < self.end_date:
            next_date = date + timedelta(days=1)
            self.log(f"Requesting data for next date: {next_date.strftime('%Y-%m-%d')}")
            yield from self.make_requests_from_date(next_date)

    def parse_temp_range(self, temp_range):
        if temp_range is None:
            return None, None

        match = re.search(r'(-?\d+)\s*°\s*/\s*(-?\d+)', temp_range)
        if match:
            min_temp = int(match.group(1))
            max_temp = int(match.group(2))
            return max_temp, min_temp
        return None, None
