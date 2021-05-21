import scrapy
from ..items import TutorialItem

class QuoteSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        items = TutorialItem()
        all_div_quotes = response.css('div.quote')
        for quotes in all_div_quotes:
            title = quotes.css('span.text::text').extract()
            author = quotes.css('.author::text').extract()
            tags = quotes.css('.tag::text').extract()
            items['title'] = title,
            items['author'] = author,
            items['tag'] = tags
            # print('the elements are {},{},{}'.format(items['title'][0],items['author'][0],items['tag'][0]))
            yield items

