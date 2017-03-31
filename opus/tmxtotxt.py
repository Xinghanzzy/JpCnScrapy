# -*- coding: utf-8 -*-
import string
import re, os
import json
import urllib2
import sys
import opencc
from lxml import etree
reload(sys)
sys.setdefaultencoding('utf-8')

f = open("ja-zh_tw.txt",'a')
cc = opencc.OpenCC('t2s')

html = etree.parse('ja-zh_tw.tmx')
print type(html)
print html
result = html.xpath('//tuv[@xml:lang="ja"]/seg/text()')
result2 = html.xpath('//tuv[@xml:lang="zh_tw"]/seg/text()')
for item1,item2 in zip(result,result2):
    f.write(item1)
    f.write('\t')
    f.write(cc.convert(item2))
    f.write("\topus ja-zh_tw.tmx\n")
print len(result)
print type(result)
print type(result[0])