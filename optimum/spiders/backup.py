# import scrapy
# from ..items import OptimumItem
# from w3lib.html import remove_tags
# import re
#
# class OptiSpider(scrapy.Spider):
#     name = 'opti'
#     allowed_domains = ['optimum-bg.com']
#     start_urls = ['http://optimum-bg.com/%d0%bd%d0%be%d0%b2%d0%b8%d0%bd%d0%b8/']
#
#     def parse(self, response):
#         articles = response.xpath('//article')
#         for article in articles:
#             article_url = article.xpath('.//div[@class="post-content"]/a/@href').get()
#             yield scrapy.Request(article_url, callback=self.parse_article)
#
#             next_page = response.xpath('//a[@class="nextpostslink"]/@href').get()
#             if next_page is not None:
#                 next_page = response.urljoin(next_page)
#                 yield scrapy.Request(next_page, callback=self.parse)
#
#     def parse_article(self, response):
#
#             title = response.xpath('//div[@class="grid_24"]/h2/text()').get()
#             regex = '<style[\S\s]*?</style>'
#             description = response.xpath('//div[@class="post-content"]//descendant-or-self::*').get()
#             description = [re.sub(regex, ' ', p.strip()) for p in description]
#             description = remove_tags(''.join(description)).strip()
#             description = re.sub(" ", ' ', description)
#             description = re.sub("\n", ' ', description)
#             description = re.sub("\t", ' ', description)
#
#             items = OptimumItem()
#             items['title'] = title,
#             items['description'] = description
#             yield items