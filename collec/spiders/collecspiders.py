# -*- coding: utf-8 -*-
from __future__ import division
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
import re
import scrapy #导入scrapy包
from bs4 import BeautifulSoup
from scrapy.http import Request ##一个单独的request的模块，需要跟进URL的时候，需要用它
from scrapy.selector import Selector
from collec.items import CollecItem


#[\u0800-\u4e00]
class Myspider(scrapy.Spider):
    name = 'collec'
    count_article = 0
    allowed_domains = ['jp.tingroom.com']
    bash_url = 'http://jp.tingroom.com/yuedu/yd300p/'
    bashurl = '.html'
    f = open('jpcn304.txt','a')
    pattern = re.compile('[\u0800-\u4e00]+')
    def start_requests(self):
        for i in range(7056, 10005):
            url = self.bash_url + str(i) + self.bashurl
            yield Request(url=url, callback=self.parse)              #??
        #yield Request('http://www.23wx.com/quanben/1', self.parse)

    def parse(self, response):
        item = CollecItem()
        item['url'] = response.url
        item['title'] = "".join(response.xpath('//div[@class="content"]/p/text()').extract())
        item['alltext'] = response.xpath('//div[@class="content"]/div/text()').extract()
        print item['title']
        self.count_article += 1
        print self.count_article
        flagn = False
        for inttt in item['alltext']:
            if len(inttt) < 20:
                continue
            #print inttt.encode("utf-8")
            #print type(inttt.encode("utf-8"))
            #print type(inttt)
            #日文
            #print re.findall(u'[\u0800-\u4e00]+',inttt.strip())
            a = re.findall(u'[\u0800-\u4e00]+',inttt.strip())
            counta = 0
            for item2 in a:
                counta += len(item2)
            #print counta
            #print counta/len(inttt.strip())
            #print "~~~~~~~~~~~~~~~   " + str(len(a)) +"  "+ str(len(inttt.strip())) + "  "+str((len(a))/len(inttt.strip())) +"   ~~~~~~~~~~~~~~~"
            probability = counta/len(inttt.strip())
            if probability > 0.26:
                print "**********Japaness**************"
                if flagn:
                    self.f.write('\t')
                    self.f.write(item['url'])
                    self.f.write("\n")
                    flagn = False
                print inttt.strip().encode("utf-8")
                item['jptext']="".join(inttt.strip().encode("utf-8"))
                print type(item['jptext'])
                print item['jptext']
                #print item['jptext'].split("\n")
                self.f.write(item['jptext'])


            else:
                print "**********Chinese**************"
                print inttt.strip().encode("utf-8")
                if flagn is False:
                    self.f.write('\t')
                self.f.write(inttt.strip().encode("utf-8"))
                flagn = True
        if flagn:
            self.f.write('\t')
            self.f.write(item['url'])
            self.f.write("\n")
            flagn = False
            print  "----------------------------------"
        print item['url']

