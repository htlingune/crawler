# crawler
#the crawler for various sites
crawl the news content from various sites and store as json per news, in which the data contain :(date, title, content, href, clicks, tag)
for the details which are not available ,fill the value as 'NA'

starting(index) site:

cnyes_news_hightlight: https://news.cnyes.com/news/cat/headline

cnyes_news_per_year: https://news.cnyes.com/news/cat/tw_stock

ltn_strategy: https://ec.ltn.com.tw/list/strategy

ltn_securities: https://ec.ltn.com.tw/list/securities

ltn_weeklybiz_investment: https://ec.ltn.com.tw/list/weeklybiz and https://ec.ltn.com.tw/list/investment

one can load the crawled json-file with the fileload.py
