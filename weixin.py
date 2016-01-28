# -*- coding: utf-8 -*-  
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )


import urllib
import urllib2
from lxml import *
import lxml.html as HTML 
from bs4 import BeautifulSoup

Keyword="网贷之家"
Keyword=urllib.quote(Keyword)
Url="http://weixin.sogou.com/weixin?type=1&query="+Keyword+"&ie=utf8"

Page=urllib2.urlopen(Url).read()

PageInHtml=HTML.document_fromstring(Page)

# TitleXpath1="//div[@class='wx-rb bg-blue wx-rb_v1 _item']/div/h3"
# TitleXpath2="//div[@class='wx-rb bg-blue wx-rb_v1 _item']/div/h3/em"
# Title1=PageInHtml.xpath(TitleXpath1)
# Title2=PageInHtml.xpath(TitleXpath2)

# for i in range(len(Title1)):
# 	print Title1[i].text,Title2[i].text

soup = BeautifulSoup(Page)
for h3 in soup.find_all('h3'):
	print h3.get_text()