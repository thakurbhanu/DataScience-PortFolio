# -*- coding: utf-8 -*-
import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['www.quotes.toscrape.com/']
    start_urls = ['http://www.quotes.toscrape.com//']

    def parse(self, response):
        title = response.css('title').extract()

        yield {
            'title text' : title
            }
