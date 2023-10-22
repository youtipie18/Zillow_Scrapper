import scrapy
from ..utils import URL, cookie_parser, parse_new_url
from ..items import ZillowItem
import json


class ZillowHousesSpider(scrapy.Spider):
    name = 'zillow_houses'
    allowed_domains = ['www.zillow.com']

    def start_requests(self):
        yield scrapy.Request(
            url=URL,
            callback=self.parse,
            cookies=cookie_parser(),
            meta={
                'currentPage': 1
            }
        )

    def parse(self, response):
        current_page = response.meta['currentPage']
        json_resp = json.loads(response.body)
        print(json_resp)
        houses = json_resp.get('cat1').get('searchResults').get('listResults')
        for house in houses:
            item = ZillowItem()
            item['id'] = house.get('id')
            item['image_urls'] = house.get('imgSrc')
            item['detail_url'] = house.get('detailUrl')
            item['status_type'] = house.get('statusType')
            item['status_text'] = house.get('statusText')
            item['price'] = house.get('price')
            item['address'] = house.get('address')
            item['beds'] = house.get('beds')
            item['baths'] = house.get('baths')
            item['area_sqft'] = house.get('area')
            item['latitude'] = house.get('latLong').get('latitude')
            item['longitude'] = house.get('latLong').get('longitude')
            item['broker_name'] = house.get('brokerName')
            item['broker_phone'] = house.get('brokerPhone')
            yield item

            total_pages = json_resp.get('cat1').get('searchList').get('totalPages')
            if current_page <= total_pages:
                current_page += 1
            yield scrapy.Request(
                url=parse_new_url(URL, page_number=current_page),
                callback=self.parse,
                cookies=cookie_parser(),
                meta={
                    'currentPage': current_page
                }
            )
