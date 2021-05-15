import scrapy
from ..items import TutorialItem

class QuoteSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
    	# ------------>1
        # title = response.css('title::text').extract()
        # # Extracts the text from the title.
        # yield {'titletext': title}
        # ------------>2
        # all_div_quotes = response.css('div.quote')
        # title = all_div_quotes.css('span.text::text').extract()
        # author = all_div_quotes.css('.author::text').extract()
        # tags = all_div_quotes.css('.tag::text').extract()

        # yield{'title': title, 'author': author, 'tags': tags}
        # ------------>3
        # all_div_quotes = response.css('div.quote')
        # for quotes in all_div_quotes:
        # 	title = quotes.css('span.text::text').extract()
        # 	author = quotes.css('.author::text').extract()
        # 	tags = quotes.css('.tag::text').extract()
 
        # 	yield{
        # 		'title': title,
        # 		'author': author,
        # 		'tags': tags
        # 	}
        # ------------>4
    	# items = TutorialItem()

    	# all_div_quotes = response.css('div.quote')
    	# for quotes in all_div_quotes:
    	# 	title = quotes.css('span.text::text').extract()
    	# 	author = quotes.css('.author::text').extract()
    	# 	tags = quotes.css('.tag::text').extract()
    	# 	items['title'] = title,
    	# 	items['author'] = author,
    	# 	items['tag'] = tags

    	# 	yield items
        # ------------>5
        items = TutorialItem()
        all_div_quotes = response.css('div.quote')

        for quotes in all_div_quotes:
        	title = quotes.css('span.text::text').extract()
        	author = quotes.css('.author::text').extract()
        	tags = quotes.css('.tag::text').extract()
        	items['title'] = title,
        	items['author'] = author,
        	items['tag'] = tags

        	yield items
        			