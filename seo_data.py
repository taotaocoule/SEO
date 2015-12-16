# -*- coding: utf-8 -*-  

# seo data
import urllib
import urllib2
from lxml import *
import lxml.html as HTML 

# KeyWord=raw_input("please input the keyword:")
KeyWord='微信'
KeyWord=urllib.quote(KeyWord)
KeyUrl='http://s.tool.chinaz.com/baidu/words.aspx?kw='+KeyWord

PageDownload=urllib2.urlopen(KeyUrl)
PageRead=PageDownload.read()

PageInHtml=HTML.document_fromstring(PageRead)
KewordXpath='//td[2]/a/span'
DataXpath='//td[3]/a'
GetXpath='//td[4]/a'
RankFirstXpath='//td[5]'
RankFirstWebXpath='//td[5]/a'

Keyword=PageInHtml.xpath(KewordXpath)
Data=PageInHtml.xpath(DataXpath)
Get=PageInHtml.xpath(GetXpath)
RankFirst=PageInHtml.xpath(RankFirstXpath)
RankFirstWeb=PageInHtml.xpath(RankFirstWebXpath)

for i in range(len(Keyword)):
	print Keyword[i].text,Data[i].text,Get[i].text,RankFirst[i].text,RankFirstWeb[i].text
	