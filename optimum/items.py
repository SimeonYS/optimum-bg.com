# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class OptimumItem(scrapy.Item):
    title = scrapy.Field()
    description = scrapy.Field()
