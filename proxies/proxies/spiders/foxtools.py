# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from proxies.items import ProxyItem
from scrapy.loader.processors import TakeFirst, MapCompose
from datetime import datetime


class FoxtoolsSpider(CrawlSpider):
    name = 'foxtools'
    allowed_domains = ['foxtools.ru']
    start_urls = ['http://foxtools.ru/Proxy']

    #working with pagination
    rules = (
        Rule(LinkExtractor(allow=r'page=\d+'), callback='parse_items', follow=True),
    )


    def parse_items(self, response):
        #selecting the table with the information
        proxies = response.xpath("//table[@id='theProxyList']/tbody/tr")
        for proxy in proxies:
            #creating the proxy item, from the selected row of the table
            proxy_item = ItemLoader(item=ProxyItem(), selector=proxy)
            #capturing proxy information
            proxy_item.add_xpath('ip', "td[2]/text()", TakeFirst())
            proxy_item.add_xpath('port', "td[3]/text()", TakeFirst(), MapCompose(int))
            proxy_item.add_xpath('protocol', "td[6]//text()", TakeFirst(), MapCompose(unicode.strip, unicode.lower))
            #adding information about the crawler
            proxy_item.add_value('url_crawl', response.url)
            proxy_item.add_value('date_crawl', datetime.now())
            yield proxy_item.load_item()

