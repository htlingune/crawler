import requests
import os
import json
import time
import datetime
import re

def req_json(url,headers):
    response = session.get(url, headers=headers)
    json = response.json()
    return json

def content(json,n):
    title = str(json['items']['data'][n]['title']).replace('<', ' ').replace('>', ' ').replace('/', '').replace('＃', '').replace('?', '').replace('*', '_').replace('\"', '_').replace(':', '_').replace('\n', '_')
    article_id = str(json['items']['data'][n]['newsId'])
    href = 'https://news.cnyes.com/news/id/' + article_id
    content_url = 'https://news.cnyes.com/api/v6/news/' + article_id
    date = time.ctime(json['items']['data'][n]['publishAt'])
    content_response = session.get(content_url, headers=headers)
    content_json = content_response.json()
    content = content_json['items']['content']
    tag = content_json['items']['keywords']
    content = text_clean(content)
    output = {'date': date, 'title': title, 'content': content, 'href': href, 'tag': tag}
    return title, output

def text_clean(content):
    if re.search(r'(<a.+?a>)', content) != None:
        content = re.sub(r"(\(<a.+?a>\))", '', content, count=0, flags=re.IGNORECASE)
    if re.search(r'(&l.+?gt;)', content) != None:
        content = re.sub(r'(&l.+?gt;)', '', content, count=0)
    if re.search(r'(&a.+?sp;)', content) != None:
        content = re.sub(r'(&a.+?sp;)', '', content, count=0)
    if re.search(r'(\n)', content) != None:
        content = content.replace('\r', '')
        content = content.replace('\n', '')
    return content

def file_save(path, title, output):
    with open(path % (title) + '.json', 'w', encoding='utf8') as f:
        json.dump(output, f)

year = 2015
path = r'./cnyesnewshistory'+r'/'+str(year)+r'/%s'
if not os.path.exists(r'./cnyesnewshistory'+r'/'+str(year)):
    os.mkdir(r'./cnyesnewshistory'+r'/'+str(year))
headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36'}

for i in range(1,12):
    starttime = int(datetime.datetime(year, i, 1).timestamp())
    endtime = int(datetime.datetime(year, i+1, 1).timestamp())
    timerange = [starttime,endtime]
    url_news_index = 'https://news.cnyes.com/api/v3/news/category/tw_stock?startAt=%s&endAt=%s' %(timerange[0],timerange[1])
    session = requests.session()
    index_json = req_json(url_news_index, headers)
    lastpage = int(index_json['items']['last_page'])
    session.close()
    for l in range(1,lastpage+1):
        url_news_page = 'https://news.cnyes.com/api/v3/news/category/tw_stock?startAt=%s&endAt=%s&page=%d' % (timerange[0], timerange[1], l)
        news_page_json = req_json(url_news_page, headers)
        data_perpage = len(news_page_json['items']['data'])
        for n in range(data_perpage):
            title, output = content(news_page_json, n)
            if not os.path.exists(path %(title)):
                session.close()
                file_save(path, title, output)
