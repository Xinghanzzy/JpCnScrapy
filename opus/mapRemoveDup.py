# -*- coding: utf-8 -*-
import string
import re
import json
import urllib2
import time
import sys
import os
import os.path
import chardet
import opencc  #opencc 太慢 这个代码抛弃了
from lxml import etree
reload(sys)
savefinal=open(r'final1.txt','w')   #打开处理后存放的文件
savedict = dict()
print type(savedict)
rootdir ="F:\CN&JP\save2"
for pattern,dirnames,filenames in os.walk(rootdir):
    print pattern
    for filename in filenames:
        fr = open(rootdir +"\\"+filename,'r')
        print filename
        line = fr.readline()
        while line:
            # fencoding = chardet.detect(line)
            # print fencoding

            listline = line.split('\t')
            if len(listline) < 3:
                line = fr.readline()
                continue
            # print line
            # print listline
            str_key = listline[0] +"\t"+ listline[1]
            str_value = listline[2]
            savedict[str_key] = str_value
            line = fr.readline()
            # if str_key in savedict.keys():
            # 	line = fr.readline()
            # 	continue
            # else:
            # 	savedict[str_key] = str_value
            # 	line = fr.readline()
        fr.close()
for (k,v) in savedict.items():
    savefinal.write(k)
    savefinal.write('\t')
    savefinal.write(v)

savefinal.close()

# print type(cikuss)
# list2 = {}.fromkeys(cikuss)     #列表去重方法，将列表数据当作字典的键写入字典，依据字典键不可重复的特性去重
# for item in list2:
# 	print item
# i=1
# for line in list2:
# 	if line[0]!=',':
# 		# print line[0:-1].decode('utf-8').encode('gbk')   #数据量太多，会出现编码报错。蛋疼
# 		print  u"写入第："+`i`+u" 个"
# 		i+=1
# 		xieci.writelines(line)
# xieci.close()
#
