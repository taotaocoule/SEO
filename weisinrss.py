# -*- coding: utf-8 -*-  
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

import urllib
import urllib2
from bs4 import BeautifulSoup
import re

query=['大数据文摘']
header={'Cookie':'CXID=364E00193E26A7AD6BE01660038E167E; SUID=6A52E765526C860A56565FE2000A2448; IPLOC=CN3100; SUV=1448516589067105; weixinIndexVisited=1; GOTO=Af99046; pgv_pvi=7942813696; ssuid=8187851612; usid=TJ3TDmEq-PTEhNsb; ld=wNtUyZllll2QWabclllllVzXnKylllllBWNvzkllllGlllllpr$8C5@@@@@@@@@@; ABTEST=4|1453876849|v1; SNUID=4E76C34125200F964AF169AC25EA0CAB; ad=Kdjpvlllll2QqO@AlllllVbjP9klllllBWNvzkllll9lllll9j7ll5@@@@@@@@@@; pgv_si=s6132648960; sct=64','Host':'weixin.sogou.com',
		'User-Agent':r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36',
		'X-Requested-With':'XMLHttpRequest'}

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
	# urlread=urlread.replace("\n","")
	# c=urlread[19:-1]
	# c=eval(c)
	return urlread

def GetDetail(keyword,data):
	k='<'+keyword+'>'+'(.*?)'+'<\\\/'+keyword+'>'
	pattern=re.compile(k)
	Detail=pattern.findall(data)
	return Detail

for i in range(len(query)):
	print GetUrlData(query[i])
	title=GetDetail('title',GetData(GetUrlData(query[i])))
	content=GetDetail('content168',GetData(GetUrlData(query[i])))
	url=GetDetail('url',GetData(GetUrlData(query[i])))
	for j in url:
		print 'http://weixin.sogou.com'+j[9:-3]

