# -*- coding: utf-8 -*-
import string
import re
import json
import urllib2
import time
import sys
import os
import os.path
from lxml import etree
from langconv import *
reload(sys)
sys.setdefaultencoding('utf-8')

print(sys.version)
print(sys.version_info)

# 转换繁体到简体
def cht_to_chs(line):
    line = Converter('zh-hans').convert(line)
    line.encode('utf-8')
    return line

# 转换简体到繁体
def chs_to_cht(line):
    line = Converter('zh-hant').convert(line)
    line.encode('utf-8')
    return line

removeTuv = re.compile('<tuv.*?>|</tuv>')
removeSeg = re.compile('<seg.*?>|</seg>')
rootdir ="F:\My Documents\Downloads\ja-zh2"
flog = open("log_tmx.txt",'a')
a = time.clock()
print '%Y-%m-%d %H-%M-%S',time.localtime(time.time())

def repace(x):
    x = re.sub(removeTuv,"",x)
    x = re.sub(removeSeg,"",x)
    x = x.replace('\t', '').replace('\n', '').replace('\r', '')
    return x.strip()

#遍历 roodir 文件夹
for pattern,dirnames,filenames in os.walk(rootdir):
    print pattern
    for filename in filenames:
        print filename.split(".")
        print '%Y-%m-%d %H-%M-%S', time.localtime(time.time())
        flog.write("Begin\n")
        flog.write(pattern)
        flog.write("\n")
        flog.write(filename)
        flog.write("\n")
        #文件名拆分 zh_*关键字
        listname = re.split('-|\s',filename)
        print listname
        #文件操作
        fr = open(rootdir +"\\"+filename,'r')
        fw = open(os.path.abspath('.') + "\\save2\\" + filename.split(".")[0] + ".txt", "a")
        line = fr.readline()
        while line:
            #print line
            if line.find('<tuv xml:lang="ja') != -1 :
                #print "----------"
                ja = repace(line)
                line = fr.readline()
                fw.write(ja)
                fw.write('\t')
                #print ja
            elif line.find('<tuv xml:lang="zh') != -1:
                zh = repace(line)
                line = fr.readline()
                zh = cht_to_chs(zh.decode("utf-8"))
                fw.write(zh)
                fw.write("\topus "+filename+"\n")

            else:
                line = fr.readline()
        fr.close()
        fw.close()
        str1 = os.path.abspath('.') + "\\save\\" + filename.split(".")[0] + ".txt"+"\nEnd\n"
        flog.write(str1)
        flog.write("----------------------------------------------------------------\n")
        flog.write("----------------------------------------------------------------\n\n\n")
        print "---------------"
