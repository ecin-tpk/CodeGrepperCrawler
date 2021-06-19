# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CodegreppercrawlerItem(scrapy.Item):
    title = scrapy.Field()
    code = scrapy.Field()
    date = scrapy.Field()
    vote = scrapy.Field()
    tags = scrapy.Field()
    posted_by = scrapy.Field()
    source_name = scrapy.Field()
    source_url = scrapy.Field()

