# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.loader import ItemLoader
from proxies.items import ProxyItem
from scrapy.loader.processors import TakeFirst, MapCompose
from datetime import datetime


class UsproxySpider(Spider):
    name = "usproxy"
    allowed_domains = ["us-proxy.org"]
    start_urls = (
        'https://www.us-proxy.org/',
    )

    def parse(self, response):
    	#selecting the table with the information
        proxies = response.xpath("//tbody//tr")
        for proxy in proxies:
        	#creating the proxy item, from the selected row of the table
        	proxy_item = ItemLoader(item=ProxyItem(), selector=proxy)
        	#capturing proxy information
        	proxy_item.add_xpath('ip', "td[1]/text()", TakeFirst())
        	proxy_item.add_xpath('port', "td[2]/text()", TakeFirst(), MapCompose(int))
        	proxy_item.add_xpath('country', "td[4]/text()", TakeFirst(), MapCompose(unicode.lower))
        	proxy_item.add_xpath('anon', "td[5]/text()", TakeFirst())
        	proxy_item.add_xpath('protocol', "td[7]/text()", TakeFirst(), MapCompose(self._filter_protocol))
        	#adding information about the crawler
        	proxy_item.add_value('url_crawl', response.url)
        	proxy_item.add_value('date_crawl', datetime.now())
        	yield proxy_item.load_item()

    def _filter_protocol(self, protocol):
    	#if yes, the protocol is https
    	if protocol and protocol=='yes':
    		return 'https'
    	return 'http'

