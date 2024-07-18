# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class QiqiharWeatherDailyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    location = scrapy.Field()
    date = scrapy.Field()
    min_temp = scrapy.Field()
    max_temp = scrapy.Field()
    status = scrapy.Field()
    moonrise = scrapy.Field()
    moonset = scrapy.Field()
    sunrise = scrapy.Field()
    sunset = scrapy.Field()

class QiqiharWeatherHourlyItem(scrapy.Item):
    location = scrapy.Field()
    date = scrapy.Field()
    time = scrapy.Field()
    temperature = scrapy.Field()
    forecast = scrapy.Field()
    rain = scrapy.Field()
    rain_percent = scrapy.Field()
    cloud = scrapy.Field()
    pressure = scrapy.Field()
    wind_speed = scrapy.Field()
    gust_speed = scrapy.Field()
    wind_direction = scrapy.Field()

    pass
