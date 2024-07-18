import scrapy
from datetime import datetime, timedelta
import re
import random
from qiqihar.items import QiqiharWeatherHourlyItem

class QiqiharWeatherHourlySpider(scrapy.Spider):
    name = "qiqihar_weather_hourly"
    allowed_domains = ["worldweatheronline.com"]
    start_urls = ["https://www.worldweatheronline.com/qiqihar-weather-history/heilongjiang/cn.aspx"]

    # custom_settings = {
    #     'FEED_FORMAT': 'jsonlines',
    #     'FEED_URI': 'qiqihar_weather_hourly.jsonl',
    #     'FEED_EXPORT_ENCODING': 'utf-8',
    # }

    def __init__(self, start_date, end_date, *args, **kwargs):
        super(QiqiharWeatherHourlySpider, self).__init__(*args, **kwargs)
        self.start_date = datetime.strptime(start_date, '%Y-%m-%d')
        self.end_date = datetime.strptime(end_date, '%Y-%m-%d')
        self.current_date = self.start_date

    def start_requests(self):
        self.log(f"Starting requests from date: {self.current_date.strftime('%Y-%m-%d')}")
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
            callback=self.parse_hourly,
            meta={'date': date, 'unique_param': response.meta['unique_param']},
            dont_filter=True
        )

    def parse_hourly(self, response):
        date = response.meta['date']
        self.log(f"Parsing hourly data for date: {date.strftime('%Y-%m-%d')}")

        rows = response.xpath(
            '//h2[text()="Weather History"]/following-sibling::div[@class="box days-box"]//tr[contains(@class, "days-details-row") and not(contains(@class, "days-details-row-header"))]'
        )

        if not rows:
            self.log(f"No data found for date: {date.strftime('%Y-%m-%d')}")

        for row in rows:
            time = row.xpath('td[1]/p[@class="days-comment"]/text()').get()
            temp = row.xpath('td[1]/p[@class="days-temp"]/text()').get()

            # 去除非数字和负号的字符，并转换为整数
            cleaned_temp_string = re.sub(r'[^\d-]', '', temp) if temp else None
            temperature = int(cleaned_temp_string) if cleaned_temp_string else None

            forecast = row.xpath('td[3]/p[@class="days-table-forecast-p"]/text()').get()

            # 去除forecast中的摄氏度符号
            cleaned_forecast_string = re.sub(r'[^\d-]', '', forecast) if forecast else None
            cleaned_forecast = int(cleaned_forecast_string) if cleaned_forecast_string else None

            rain = row.xpath('td[4]/div/div[@class="days-rain-number"]/text()').get()
            rain_percent = row.xpath('td[5]/text()').get()
            cloud = row.xpath('td[6]/text()').get()
            pressure = row.xpath('td[7]/text()').get()
            wind_speed = row.xpath('td[8]/div[@class="days-wind-number"]/text()').get()
            gust_speed = row.xpath('td[9]/div[@class="days-wind-number"]/text()').get()

            wind_direction_style = row.xpath('td[10]/div/svg/@style').get()
            wind_direction = self.parse_wind_direction(wind_direction_style)

            items = QiqiharWeatherHourlyItem(
                location='qiqihar',
                date=date.strftime('%Y-%m-%d'),
                time=time,
                temperature=temperature,
                forecast=cleaned_forecast,
                rain=rain,
                rain_percent=rain_percent,
                cloud=cloud,
                pressure=pressure,
                wind_speed=wind_speed,
                gust_speed=gust_speed,
                wind_direction=wind_direction
            )
            self.log(f"Yielding data: {items}")
            yield items
            print(items)

        # Check if there is a next date to process
        if date < self.end_date:
            next_date = date + timedelta(days=1)
            self.log(f"Requesting data for next date: {next_date.strftime('%Y-%m-%d')}")
            yield from self.make_requests_from_date(next_date)

    def parse_wind_direction(self, style):
        if style is None:
            return 'Unknown'

        match = re.search(r'rotate\((\d+\.?\d*)deg\)', style)
        if match:
            angle = float(match.group(1))
            return self.angle_to_direction(angle)
        return 'Unknown'

    def angle_to_direction(self, angle):
        directions = [
            "North", "North-Northeast", "Northeast", "East-Northeast", "East",
            "East-Southeast", "Southeast", "South-Southeast", "South",
            "South-Southwest", "Southwest", "West-Southwest", "West",
            "West-Northwest", "Northwest", "North-Northwest"
        ]
        index = round(angle / 22.5) % 16
        return directions[index]
