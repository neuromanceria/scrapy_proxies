# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class ProxyItem(Item):
    ip = Field()
    port = Field()
    country = Field()
    anon = Field()
    protocol = Field()

    url_crawl = Field()
    date_crawl = Field()
