# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from stack.items import StackItem
class StackSpiderSpider(scrapy.Spider):
    name = "stack_spider"
    allowed_domains = ["stackoverflow.com"]
    start_urls = (
        'http://www.stackoverflow.com/',
    )

    def parse(self, response):
        questions = Selector(response).xpath('//div[@class="summary"]/h3')
        for question in questions:
            item = StackItem()
            item['title'] = question.xpath('a[@class="question-hyperlink"]/text()').extract()[0]
            item['url'] = question.xpath('a[@class="question-hyperlink"]/@href').extract()[0]
            yield item
            
        
