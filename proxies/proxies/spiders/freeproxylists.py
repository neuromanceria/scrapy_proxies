# -*- coding: utf-8 -*-
import scrapy


class FreeproxylistsSpider(scrapy.Spider):
    name = "freeproxylists"
    allowed_domains = ["freeproxylists.net"]
    start_urls = (
        'http://www.freeproxylists.net/',
    )

    def parse(self, response):
        pass
