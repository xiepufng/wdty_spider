# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WdtyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name=scrapy.Field()
    expected_rate_of_interest=scrapy.Field()
    status=scrapy.Field()
    capital=scrapy.Field()
    adress=scrapy.Field()
    time=scrapy.Field()
    product_info=scrapy.Field()
