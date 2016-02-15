# -*- coding: utf-8 -*-  
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

import urllib
import urllib2
from bs4 import BeautifulSoup
import re

query=['大数据文摘','网贷之家']

def GetUrlData(query):
	query=urllib.quote(query)
	url=r"http://weixin.sogou.com/weixin?type=1&query="+query+r"&ie=utf8"
	urlopen=urllib.urlopen(url)
	urlread=urlopen.read()
	soup=BeautifulSoup(urlread)
	url=soup.find(id="sogou_vr_11002301_box_0")
	href=url.get('href')
	href=href[5:]
	url=r"http://weixin.sogou.com/gzhjs?"+href+r"&cb=sogou.weixin_gzhcb&page=1&gzhArtKeyWord=&tsn=0&t=1455506682975&_=1455506682687"
	return url

def GetData(url):
	urlopen=urllib.urlopen(url)
	urlread=urlopen.read()
	urlread=urlread.replace("\n","")
	c=urlread[19:-1]
	c=eval(c)
	return c

for i in range(len(query)):
	print GetUrlData(query[i])
	print GetData(GetUrlData(query[i]))
