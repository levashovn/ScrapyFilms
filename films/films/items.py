# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class KinopoiskItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    movie_id = scrapy.Field()
    title = scrapy.Field()
    recommended = scrapy.Field()
    genre = scrapy.Field()
    date = scrapy.Field()
    country = scrapy.Field()
    director = scrapy.Field()

class AmediatekaItem(scrapy.Item):
    item_id = scrapy.Field()
    title = scrapy.Field()
    genre = scrapy.Field()


