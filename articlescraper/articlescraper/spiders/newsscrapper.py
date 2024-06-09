import scrapy
from articlescraper.items import ArticlescraperItem


class NewsscrapperSpider(scrapy.Spider):
    name = "newsscrapper"
    allowed_domains = ["www.theguardian.com"]
    start_urls = ["https://www.theguardian.com/international"]

    def parse(self, response):
        main_page_urls = '//a[contains(@class, "dcr-lv2v9o")]/@href'
        for news_url in response.xpath(main_page_urls).extract():
            yield scrapy.Request(
                    url="https://www.theguardian.com"+news_url,
                    callback=self.parsearticle
            )
    
    def parsearticle(self,response):

        author = '//*[contains(@class,"dcr-1cfpnlw")]//text()'
        title = '//div[contains(@data-gu-name, "headline") or contains(@class, "headline")]//h1//text()'
        subtitle = '//*[contains(@data-gu-name,"standfirst")]//p//text()'
        content = '//*[contains(@class,"article-body")]//p//text()'
        published_at = '//*[contains(@class,"dcr-u0h1qy")]//text()'

        item = ArticlescraperItem()

        item['author'] = response.xpath(author).extract()
        item['title']= response.xpath(title).extract()
        item['subtitle' ]= ''.join(response.xpath(subtitle).extract())
        item['content' ]= ''.join(response.xpath(content).extract())
        item['published_at'] = response.xpath(published_at).extract()
        item['url']=  response.request.url

        yield item

