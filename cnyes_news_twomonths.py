import requests
from bs4 import BeautifulSoup
import os
import json
import time
path =r'./cnyesnewshistory/%s'
if not os.path.exists(r'./cnyesnewshistory'):
    os.mkdir(r'./cnyesnewshistory')
headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36'}
timerange = [1451577600,1456761600]
url_news_index = 'https://news.cnyes.com/api/v3/news/category/tw_stock?startAt=%s&endAt=%s' %(timerange[0],timerange[1])
session = requests.session()
response = session.get(url_news_index, headers = headers)
index_json = response.json()
lastpage = index_json['items']['last_page']
data_perpage = len(index_json['items']['data'])
for n in range(data_perpage):
    title = index_json['items']['data'][n]['title']
    article_id = str(index_json['items']['data'][n]['newsId'])
    content_url = 'https://news.cnyes.com/api/v6/news/' + article_id
    date = time.ctime(index_json['items']['data'][n]['publishAt'])
    content_response = session.get(content_url, headers = headers)
    content_json = content_response.json()
    content = content_json['items']['content']
    tag = content_json['items']['keywords']
    href = 'https://news.cnyes.com/news/id/' + article_id
    output = {'date':date,'title':title,'content':content,'href':href,'tag':tag}
    if not os.path.exists(path %(title)):
        with open(path %(title) + '.json', 'w', encoding='utf8') as f:
            json.dump(output,f)
session.close()