# crawler practices
the crawler for various sites that contain the news related to taiwanese stock market
crawl the news content from various sites and store as json per news, in which json contain :(date, title, content, href, clicks, tag)
for the details which are not available ,fill the value as 'NA'

daily crawler:
cnyes_news_hightlight.py, ltn_strategy.py, ltn_securities.py, ltn_investment.py, ltn_weeklybiz_oneweek.py, ltn_RSS.py ,daily_multiprocess_que.py


the reference site:

cnyes_news_hightlight.py: https://news.cnyes.com/news/cat/headline

cnyes_news_history.py: https://news.cnyes.com/news/cat/tw_stock

ltn_strategy.py: https://ec.ltn.com.tw/list/strategy

ltn_securities.py: https://ec.ltn.com.tw/list/securities

ltn_investment.py: https://ec.ltn.com.tw/list/investment

ltn_all_history.py: https://ec.ltn.com.tw/list/strategy, https://ec.ltn.com.tw/list/securities and https://ec.ltn.com.tw/list/investment

ltn_weeklybiz_history.py and ltn_weeklybiz_oneweek.py: https://ec.ltn.com.tw/list/weeklybiz

ltn_RSS.py: https://news.ltn.com.tw/rss/business.xml

live_stock_price: https://mis.twse.com.tw/stock/index.jsp

For efficiency daily_multiprocess_que.py, using multithread to crawl the sites which update on daily bases 

one can load the crawled json-file with fileload.py
