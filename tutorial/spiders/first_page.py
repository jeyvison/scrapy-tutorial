import scrapy


class FirstPage(scrapy.Spider):
    name = 'firstpage'
    start_urls = ['http://www.bbc.com']


    def parse(self, response):
        for article in response.css('a.block-link__overlay-link'):
            yield{
                    'text': article.css('::text').extract_first(),
                    'link': article.css('::attr(href)').extract_first(),
                    }
