# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ZillowItem(scrapy.Item):
    id = scrapy.Field()
    image_urls = scrapy.Field()
    detail_url = scrapy.Field()
    status_type = scrapy.Field()
    status_text = scrapy.Field()
    price = scrapy.Field()
    address = scrapy.Field()
    beds = scrapy.Field()
    baths = scrapy.Field()
    area_sqft = scrapy.Field()
    latitude = scrapy.Field()
    longitude = scrapy.Field()
    broker_name = scrapy.Field()
    broker_phone = scrapy.Field()
