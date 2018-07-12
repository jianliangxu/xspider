# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SxspiderItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    image_urls = scrapy.Field()
    page = scrapy.Field()
    file_urls = scrapy.Field()
    files = scrapy.Field()
