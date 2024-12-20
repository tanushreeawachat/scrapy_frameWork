# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import Join, MapCompose, TakeFirst
from w3lib.html import remove_tags

def covertPrice(price):
    print('convertPrice')
    print('convertPrice')
    print('convertPrice')
    print('Price',price )
    print('convertPrice')
    print('convertPrice')
    print('convertPrice')
    return f'convertPrice-{price}'

class FlipkartItem(scrapy.Item):
    title = scrapy.Field(
        input_processor=MapCompose(remove_tags),
        output_processor=TakeFirst(),
    )
    price = scrapy.Field(
        input_processor=MapCompose(remove_tags, covertPrice),
        output_processor=TakeFirst(),
    )
