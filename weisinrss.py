# -*- coding: utf-8 -*-  
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

import urllib
import urllib2
from bs4 import BeautifulSoup
import re
import cookielib
from selenium import webdriver

query=['大数据文摘']
# cookie=r'CXID=364E00193E26A7AD6BE01660038E167E; SUID=6A52E765526C860A56565FE2000A2448; IPLOC=CN3100; SUV=1448516589067105; weixinIndexVisited=1; GOTO=Af99046; pgv_pvi=7942813696; ssuid=8187851612; usid=TJ3TDmEq-PTEhNsb; ld=wNtUyZllll2QWabclllllVzXnKylllllBWNvzkllllGlllllpr$8C5@@@@@@@@@@; ABTEST=4|1453876849|v1; sct=64; ad=aNjpvlllll2QqO@AlllllVbRTi9lllllBWNvzkllll9lllll9v7ll5@@@@@@@@@@; SNUID=546CDA583E3815D3E50EEAE63EDBCAC1'

def GetCookie(url):
	# url=r'https://www.sogou.com/'
	# cookie=cookielib.MozillaCookieJar()
	# handler=urllib2.HTTPCookieProcessor(cookie)
	# opener=urllib2.build_opener(handler)
	# response=opener.open(url)
	# cookie=cookie
	# a=''
	# for item in cookie:
	# 	a=a+item.name+'='+item.value+';'
	# cookie=a[0:-1]
	# cookie=r'IPLOC=CN3100; SUID=6A52E7655FC00D0A000000005694A6C1; SUV=1452582594666858; sct=1; SNUID=82BB0F8DE8ECC4BB36A6FB93E90245B0; LSTMV=254%2C221; LCLKINT=599952'
	driver=webdriver.Firefox()
	driver.get(url)
	cookies=driver.get_cookies()
	cookie=""
	for i in cookies:
		cookie=cookie+i['name']+'='+i['value']+';'
	cookie=cookie[:-1]	
	header={'Cookie':cookie,
		'Host':'weixin.sogou.com',
		'User-Agent':r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36',
		'X-Requested-With':'XMLHttpRequest'}
	return header

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

def GetData(url,header):
	req=urllib2.Request(url,headers=header)
	text=urllib2.urlopen(req)
	text=text.read()
	return text
	# urlopen=urllib.urlopen(url)
	# urlread=urlopen.read()
	# urlread=urlread.replace("\n","")
	# c=urlread[19:-1]
	# c=eval(c)
	# return urlread

def GetDetail(keyword,data):
	k='<'+keyword+'>'+'(.*?)'+'<\\\/'+keyword+'>'
	pattern=re.compile(k)
	Detail=pattern.findall(data)
	return Detail

cookie=GetCookie(GetUrlData(query[0]))
for i in range(len(query)):
	print GetUrlData(query[i])
	print cookie
	data=GetData(GetUrlData(query[i]),cookie)
	title=GetDetail('title',data)
	content=GetDetail('content168',data)
	url=GetDetail('url',data)
	for j in range(len(title)):
		print title[j][9:-3]
		print content[j][9:-3]
		print 'http://weixin.sogou.com'+url[j][9:-3]

