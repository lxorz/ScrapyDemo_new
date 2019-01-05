# -*- coding: utf-8 -*-
import scrapy
from FirstDome.items import FirstdomeItem

class FirstbloodSpider(scrapy.Spider):
    name = 'FirstBlood'
    #allowed_domains = ['www.baidu.com']
    start_urls = ['http://datachart.500.com/ssq/history/newinc/history.php?limit=100&sort=0']
    #url = 'http://datachart.500.com/ssq/history/history.shtml'


    def parse(self, response):
        i = 0
        div_list = response.xpath('//div[@class="chart"]/table/tbody[1]/tr')
        for div in div_list:
            qihao = div.xpath('./td[1]/text()').extract_first()
            red1 = div.xpath('./td[2]/text()').extract_first()
            red2 = div.xpath('./td[3]/text()').extract_first()
            red3 = div.xpath('./td[4]/text()').extract_first()
            red4 = div.xpath('./td[5]/text()').extract_first()
            red5 = div.xpath('./td[6]/text()').extract_first()
            red6 = div.xpath('./td[7]/text()').extract_first()
            blue = div.xpath('./td[8]/text()').extract_first()
            i+=1
            print("%s %s" %(i,qihao))
            item = FirstdomeItem()
            item['qihao'] = qihao
            item['red1'] = red1
            item['red2'] = red2
            item['red3'] = red3
            item['red4'] = red4
            item['red5'] = red5
            item['red6'] = red6
            item['blue'] = blue

            yield item
