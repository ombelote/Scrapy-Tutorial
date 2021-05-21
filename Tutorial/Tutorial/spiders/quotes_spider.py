import scrapy
from ..items import TutorialItem

class QuoteSpider(scrapy.Spider):
	name = 'quotes'
	# start_urls = ['http://quotes.toscrape.com/']

	# def parse(self, response):

	# 	items = TutorialItem()
	# 	all_div_quotes = response.css('div.quote')

	# 	for quotes in all_div_quotes:
	# 		title = quotes.css('span.text::text').extract()
	# 		author = quotes.css('.author::text').extract()
	# 		tags = quotes.css('.tag::text').extract()
	# 		items['title'] = title,
	# 		items['author'] = author,
	# 		items['tag'] = tags

	# 		yield items
	# 	# TO follow the pages which can be changed through the address bar
	# 	next_page = response.css('li.next a::attr(href)').get()
	# 	if next_page is not None:
	# 		yield response.follow(next_page,callback = self.parse)

	#...To Do This Using Pagify

	start_urls = ['http://quotes.toscrape.com/page/1/']
	page_number = 2
	
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

			yield items
		# TO follow the pages which can be changed through the address bar
		next_page = 'http://quotes.toscrape.com/page/'+ str(QuoteSpider.page_number) + '/'
		if QuoteSpider.page_number<11:
			QuoteSpider.page_number+=1
			yield response.follow(next_page,callback = self.parse)