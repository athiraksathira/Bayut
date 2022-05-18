# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BayutItem(scrapy.Item):
    # define the fields for your item here like:
     href1 = scrapy.Field()
class BayutItem2(scrapy.Item) :
    property_info=scrapy.Field()
    price=scrapy.Field()
    currency=scrapy.Field()
    amount = scrapy.Field()
    location=scrapy.Field()
    bed=scrapy.Field()
    bath=scrapy.Field()
    size=scrapy.Field()
    bed_bath_size=scrapy.Field()

    permit_no=scrapy.Field()
    agent_name=scrapy.Field()
    url=scrapy.Field()
    breadcrumbs=scrapy.Field()
    amenities=scrapy.Field()
    description=scrapy.Field




