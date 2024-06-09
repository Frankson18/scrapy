# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ArticlescraperItem(scrapy.Item):
    author = scrapy.Field()
    title = scrapy.Field()
    subtitle = scrapy.Field()
    content = scrapy.Field()
    published_at = scrapy.Field()
    url = scrapy.Field()
    pass
