# -*- coding: utf-8 -*-  

# seo data
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

import urllib
import urllib2
from lxml import *
import lxml.html as HTML 

KeyUrl='http://club.excelhome.net/'
FirstPage='http://club.excelhome.net/forum.php'

PageDownload=urllib2.urlopen(FirstPage)
PageRead=PageDownload.read()

PageInHtml=HTML.document_fromstring(PageRead)
KewordXpath=r"//div[@id='portal_block_19_content']/div/div/a"
KeywordUrlXpath=r"//div[@id='portal_block_19_content']/div/div/a/@href"

Keyword=PageInHtml.xpath(KewordXpath)
KeywordUrl=PageInHtml.xpath(KeywordUrlXpath)
for i in range(len(Keyword)):
	url=KeyUrl + KeywordUrl[i].strip()
	print Keyword[i].text,url
	
