# -*- coding: utf-8 -*-
import scrapy


class FoxtoolsSpider(scrapy.Spider):
    name = "foxtools"
    allowed_domains = ["foxtools.ru"]
    start_urls = (
        'http://foxtools.ru/Proxy',
    )

    def parse(self, response):
        pass
