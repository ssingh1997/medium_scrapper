# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class N2ProjectItem(scrapy.Item):
    author_url = scrapy.Field()
    author_name = scrapy.Field()
    article_url = scrapy.Field()
    article_name = scrapy.Field()
    search_tags = scrapy.Field()
    twitter_handle = scrapy.Field()
    pass
