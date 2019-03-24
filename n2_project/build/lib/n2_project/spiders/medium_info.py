# -*- coding: utf-8 -*-
import scrapy
from ..items import N2ProjectItem




class MediumInfoSpider(scrapy.Spider):
    name = 'medium_info'
    handle_httpstatus_list = [401, 400]
    autothrottle_enabled = True
    search_string = input()


    start_urls = ["https://medium.com/search?q="+search_string]

    def parse(self, response):

      items = N2ProjectItem()

      for article_info in response.xpath("//div[@class='js-searchResults']"):
        author_url = article_info.xpath("//a[@class='link u-baseColor--link avatar']/@href").extract()
        for url in author_url:
          yield scrapy.Request(url=url, callback=self.parse_handles)

      for article_info in response.xpath("//div[@class='js-searchResults']"):
        author_url = article_info.xpath("//a[@class='link u-baseColor--link avatar']/@href").extract(),
        author_name = article_info.xpath("//a[@class='ds-link ds-link--styleSubtle link link--darken link--accent u-accentColor--textNormal u-accentColor--textDarken']/text()").extract(),
        article_url = article_info.xpath("//a[@class='button button--smaller button--chromeless u-baseColor--buttonNormal']/@href").extract(),
        article_name = article_info.xpath("//h3[@class='graf graf--h3 graf-after--figure graf--title']/text()").extract(),
        search_tags = article_info.xpath("//a[@class='link u-baseColor--link']/text()").extract()

        items['author_url'] = author_url
        items['author_name'] = author_name
        items['article_url'] = article_url
        items['article_name'] = article_name
        items['search_tags'] = search_tags

        yield items

    def parse_handles(self, response):

      items = N2ProjectItem()

      for handle in response.xpath("//div[@class='root']"):

         twitter_handle = handle.xpath("/div[2]/div[4]/span/div/div[4]/div/a/@href").extract()

         items['twitter_handle'] = twitter_handle

         yield items














