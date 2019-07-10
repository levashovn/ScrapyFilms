# -*- coding: utf-8 -*-
from kinopoisk.items import KinopoiskItem
from scrapy import Spider
from scrapy.http import Request


class KinopoiskSpider(Spider):
    name = 'Kinopoisk'
    allowed_domains = ['films.ru']
    start_urls = ['https://www.films.ru/top/lists/322/filtr/all/sort/votes/']

    def parse(self, response):
        films = response.xpath("*//div[@class='poster']/a/@href").extract()
        for film in films:
            absolute_url = 'https://www.films.ru' + film
            yield Request(absolute_url, callback=self.parse_film)
        if not response.xpath("//div[@class='navigator']//li[@class='arr'][3]/a/@href"):
            next_page_url = response.xpath("//div[@class='navigator']//li[@class='arr'][1]/a/@href").extract_first()
        # process next page
        else:
            next_page_url = response.xpath("//div[@class='navigator']//li[@class='arr'][3]/a/@href").extract_first()
        absolute_next_page_url = 'https://www.films.ru' + str(next_page_url)
        yield Request(absolute_next_page_url)


    def parse_film(self, response):
        item = KinopoiskItem()
        item['platform'] = 'Kinopoisk'
        item['title'] = response.xpath('//h1[@class="moviename-big"]/text()').extract_first()
        item['director'] = response.xpath('//td[@itemprop="director"]//a/text()').extract_first()
        item['genre'] = response.xpath('//span[@itemprop="genre"]//a/text()').extract_first()
        temp_dict = response.url.split('/')
        item['movie_id'] = '/' + temp_dict[-3] + '/' + temp_dict[-2] + '/'
        item['date'] = response.xpath('//meta[@itemprop="dateCreated"]/@content').extract_first()
        item['country'] = response.xpath('//table[@class="info"]//tr[2]//a/text()').extract_first()
        yield Request(url=response.url + 'like/', callback=self.parse_like, meta={'item': item})

    ## THIS NEEDS TO BE REWORKED TO ONLY GET LIKE ITEMS
    def parse_like(self, response):
        old_item = response.request.meta['item']
        old_item['recommended'] = response.xpath('//a[@class=" b_gray i_orig"]').xpath('@href').extract()
        return [old_item]