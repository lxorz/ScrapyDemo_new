# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class FirstdomePipeline(object):
    fp = None

    def open_spider(self,spider):
        print('start spider..')
        self.fp = open("caipiao.txt","w",encoding='utf-8')

    def process_item(self,item,spider):
        qihao = item['qihao']
        red1 = item['red1']
        red2 = item['red2']
        red3 = item['red3']
        red4 = item['red4']
        red5 = item['red5']
        red6 = item['red6']
        blue = item['blue']
        self.fp.write(qihao + ": " + red1 + " " + red2 + " " + red3 + " " + red4 + " " + red6 + " " + blue +"\n")
        return item

    def close_spider(self,spider):
        print("end spider..")
        self.fp.close()
