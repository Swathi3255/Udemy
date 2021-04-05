# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class UdemyItem(scrapy.Item):
    # define the fields for your item here like:
    Url = scrapy.Field()
    Category = scrapy.Field()
    Course_Name = scrapy.Field()
    Best_Seller = scrapy.Field()
    Star = scrapy.Field()
    Rating = scrapy.Field()
    Students = scrapy.Field()
    Instructor = scrapy.Field()
    Price = scrapy.Field()
    Lecture_Hours = scrapy.Field()

    pass
