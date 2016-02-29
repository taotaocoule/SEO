# SEO
SEO系列脚本旨在通过python脚本快速获取需要的信息。
在我们的工作生活中，可能会涉及到很多的重复运动，比如搜集竞争对手发出的微信文章、关键词的排名情况等，这些活动都可以通过python脚本来处理，以此缩短我们重复劳动的时间。

>本系列python脚本全部基于python 2.7
>需要依赖于urllib、urllib2、re、selenium、lxml、beautifulsoup包

##seo_data.py
通过站长之家获得相关关键词的信息情况。
>依赖于urllib、urllib2、lxml
站长之家的关键词信息数据对于搜索引擎优化和营销有着很好的作用。通过分析发现站长之家的关键词信息网站是一个可直接获取的页面，且url规则非常简单，为'http://s.tool.chinaz.com/baidu/words.aspx?kw=关键词'形式。所以本段脚本直接模拟打开对应url。通过分析页面源码发现关键词信息页面元素非常整齐，适合xml格式提取，所以通过python lxml包获取页面中关键词、排名、相关站点等信息。




how to use: input the keyword
