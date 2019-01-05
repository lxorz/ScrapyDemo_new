# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
from wangyiPro.items import WangyiproItem

class WangyiSpider(scrapy.Spider):
    name = 'wangyi'
    #allowed_domains = ['www.baidu.com']
    start_urls = ['https://news.163.com']

    def __init__(self):
        #实例化一个浏览器对象
        self.bro = webdriver.Chrome(executable_path="C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")

    def close(self,spider):
        print("end spider")
        self.bro.quit()

    def parse(self, response):
        #解析国内，国际，军事，航空四个板块
        lis = response.xpath('//div[@class="ns_area list"]/ul/li')
        indexs = [3,4,6,7]
        li_list = []
        for index in indexs:
            li_list.append(lis[index])
        for li in li_list:
            url = li.xpath('./a/@href').extract_first()
            title = li.xpath('./a/text()').extract_first()

            #print(url+": "+title)
            #对每一个板块对应的url发起请求，获取页面数据（标题，缩略图，关键字，发布时间，url）
            yield scrapy.Request(url=url, callback=self.parseSecond,meta={'title':title})


    def parseSecond(self,response):
        div_list = response.xpath('//div[@class="data_row news_photoview clearfix"]')
        for div in div_list:
            head = div.xpath('.//div[@class="news_title"]/h3/a/text()').extract_first()
            url = div.xpath('.//div[@class="news_title"]/h3/a/@href').extract_first()
            imgUrl = div.xpath('./a/img/@src').extract_first()
            tag = div.xpath('.//div[@class="news_tag"]//text()').extract()
            tag = "".join(tag)
            #获取meta传过来的数据
            title = response.meta['title']
            #实例化item对象，将解析到的数据值存到item对象中
            item=WangyiproItem()
            item['head'] = head
            item['url'] = url
            item['imgUrl'] = imgUrl
            item['tag'] = tag
            item['title'] =title

            #对url发情请求，获取对应页面中存储的新闻内容数据
            yield scrapy.Request(url=url,callback=self.getContent,meta={'item':item})


    def getContent(self,response):
        #获取item传过来的数据
        item = response.meta['item']

        #解析当前页面中存储的新闻数据
        content_list = response.xpath('//div[@class="post_text"]/p/text()').extract()
        content = "".join(content_list)
        item['content'] = content

        yield item