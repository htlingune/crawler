# crawler practices
the crawler for various sites that contain the news related to taiwanese stock market
crawl the news content from various sites and store as json per news, in which the data contain :(date, title, content, href, clicks, tag)
for the details which are not available ,fill the value as 'NA'

the reference site:

cnyes_news_hightlight: https://news.cnyes.com/news/cat/headline

cnyes_news_per_year: https://news.cnyes.com/news/cat/tw_stock

ltn_strategy: https://ec.ltn.com.tw/list/strategy

ltn_securities: https://ec.ltn.com.tw/list/securities

ltn_all: https://ec.ltn.com.tw/list/strategy, https://ec.ltn.com.tw/list/securities and https://ec.ltn.com.tw/list/investment

ltn_weeklybiz: https://ec.ltn.com.tw/list/weeklybiz

ltn_RSS :using RSS provided by ltn to crawl the news per days

one can load the crawled json-file with fileload.py
