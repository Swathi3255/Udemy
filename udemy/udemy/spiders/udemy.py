import scrapy
from ..items import UdemyItem
import json

class Udemy(scrapy.Spider):
	name = 'udemy'
	allowed_domains = ['www.udemy.com']

	def start_requests(self):
		with open('links.txt','r')as f:
			links = [l.strip() for l in f.readlines()]

		for link in links:
			yield scrapy.Request('https://www.udemy.com'+link,callback=self.parse)

	#https://proxyscrape.com/free-proxy-list
	def parse(self,response):
		item = UdemyItem()
		item['Url'] = response.url
		item['Category'] = ''.join([i+' > ' for i in response.xpath('//div[@class="topic-menu udlite-breadcrumb"]/a[@class="udlite-heading-sm"]/text()').extract()])[:-3]
		item['Course_Name'] = response.xpath('normalize-space(string(//h1))').extract_first()
		item['Best_Seller'] = response.xpath('normalize-space(string(//span[contains(@class,"udlite-badge-bestseller")]))').extract_first()
		xx = json.loads(response.xpath('//div[@class="ud-component--course-landing-page-udlite--rating"]/@data-component-props').extract_first())
		item['Rating'] = xx['num_reviews']
		item['Star'] = response.xpath('normalize-space(string(//span[contains(@class,"star-rating--dark-background--Rqadv")]/span[@data-purpose="rating-number"]))').extract_first()
		item['Students'] = response.xpath('normalize-space(substring-before(//div[@data-purpose="enrollment"]," students"))').extract_first()
		item['Instructor'] = response.xpath('normalize-space(string(//div[@class="udlite-heading-lg instructor--instructor__title--34ItB"]))').extract_first()
		item['Price'] = response.xpath('normalize-space(string(//div[contains(@class,"udlite-clp-discount-price")]/span/span))').extract_first()
		item['Lecture_Hours'] = response.xpath('normalize-space(string(//span[@data-purpose="video-content-length"]))').extract_first()
		yield item
