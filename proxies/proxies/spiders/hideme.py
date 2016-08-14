# -*- coding: utf-8 -*-
from scrapy import Spider, Request
from urlparse import urljoin
from scrapy.loader import ItemLoader
from proxies.items import ProxyItem
from scrapy.loader.processors import TakeFirst, MapCompose
from datetime import datetime


class HidemeSpider(Spider):
    name = "hideme"
    allowed_domains = ["hideme.ru"]
    start_urls = (
        'http://hideme.ru/proxy-list/#list',
    )

    def parse(self, response):
    	#working with pagination
        pagination = response.xpath("//li[@class='arrow__right']/a/@href").extract()
        if pagination:
        	yield Request(urljoin(response.url, pagination[0]), callback=self.parse)
       	#selecting the table with the information
       	proxies = response.xpath("//table[@class='proxy__t']/tbody/tr")
       	for proxy in proxies:
       		#creating the proxy item, from the selected row of the table
            proxy_item = ItemLoader(item=ProxyItem(), selector=proxy)
            #capturing proxy information
            proxy_item.add_xpath('ip', "td[1]/text()", TakeFirst())
            proxy_item.add_xpath('port', "td[2]/text()", TakeFirst(), MapCompose(int))
            proxy_item.add_xpath('country', "td[3]/div/text()", TakeFirst(), MapCompose(unicode.strip, unicode.lower))
            proxy_item.add_xpath('protocol', "td[5]//text()", TakeFirst(), MapCompose(unicode.strip, unicode.lower))
            #adding information about the crawler
            proxy_item.add_value('url_crawl', response.url)
            proxy_item.add_value('date_crawl', datetime.now())
            yield proxy_item.load_item()



