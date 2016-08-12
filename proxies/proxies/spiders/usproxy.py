# -*- coding: utf-8 -*-
import scrapy


class UsproxySpider(scrapy.Spider):
    name = "usproxy"
    allowed_domains = ["https://www.us-proxy.org/"]
    start_urls = (
        'http://www.https://www.us-proxy.org//',
    )

    def parse(self, response):
        pass
