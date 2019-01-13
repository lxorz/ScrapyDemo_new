# -*- coding: utf-8 -*-
import scrapy


class FirstproSpider(scrapy.Spider):
    name = 'Firstpro'
    #allowed_domains = ['www.baidu.com']
    start_urls = ['http://datachart.500.com/']

    def parse(self, response):
        li_list = response.xpath('.//div[@class="chart_nav"]/ul[@class="sogo-cz-list clearfix"]/li')
        for li in li_list:
            url = li.xpath('.//a/@href').extract_first()
            next_url = response.urljoin(url)
            yield scrapy.Request(url=next_url, callback=self.secondspider)

    def secondspider(self,response):
        div_list = response.xpath('.//div[@class="menu-in"]')
        ul = div_list.xpath('.//ul[@class="menu"]')
        #print("2:%s" %ul)
        #li_test = ul.xpath('.//li/h2/a/text()').extract()[3]

        a_url=ul.xpath('.//li/h2/a/@href').extract()[3]

        a_text=ul.xpath('.//li/h2/a/text()').extract()[3]
        #print("2.2:%s,%s" %(a_text,a_url))
        if "历史数据" in a_text:
            next_url = response.urljoin(a_url)
            yield scrapy.Request(url=next_url,callback=self.thirdspider,meta={"url":a_url})

    def thirdspider(self,response):
        a_url =response.meta['url']
        table = []
        tbody_list = response.xpath('.//table[@id="tablelist"]')
        if len(tbody_list) >0:
            tr_list = tbody_list.xpath('.//tbody[last()]/tr')
            tr_list = response.xpath('//div[@class="chart"]/table/tbody[1]/tr')
            td_list = tr_list.xpath('.//td')
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
                print(qihao,red1,red2,red3,red4,red5,red6)
                # item = FirstdomeItem()
                # item['qihao'] = qihao
                # item['red1'] = red1
                # item['red2'] = red2
                # item['red3'] = red3
                # item['red4'] = red4
                # item['red5'] = red5
                # item['red6'] = red6
                # item['blue'] = blue
                # yield item
        #     for div in tr_list:
        #         tr=[]
        #         td_list = tr_list.xpath('.//td')
        #         for td in td_list:
        #             ret = td.xpath('./text()').extract_first()
        #             tr.append(ret)
        #         table.append(tr)
        #         table.append('\n')
        # item = FirstproItem()
        # item['table'] = table
        # print(table)

                # item = FirstdomeItem()
                # item['qihao'] = qihao
                # item['red1'] = red1
            #     item['red2'] = red2
            #     item['red3'] = red3
            #     item['red4'] = red4
            #     item['red5'] = red5
            #     item['red6'] = red6
            #     item['blue'] = blue


