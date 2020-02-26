import requests
from bs4 import BeautifulSoup
import os
import json
import time
if not os.path.exists(r'./cnyesnewstoday'):
    os.mkdir(r'./cnyesnewstoday')
headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36'}
url_news_index = 'https://news.cnyes.com/news/cat/tw_stock?exp=a'
session = requests.session()
response = session.get(url_news_index, headers = headers)
soup = BeautifulSoup(response.text, 'html.parser')
path =r'./cnyesnewstoday/%s'
for n in range(len(soup.select('a[class="_1Zdp"]'))):
    title = soup.select('a[class="_1Zdp"]')[n]['title']
    if os.path.exists(path %(title) + '.json'):
        break
    article_id = soup.select('a[class="_1Zdp"]')[n]['href']
    id = article_id.split('/')[-1]
    date = soup.select('a[class="_1Zdp"]')[n].time['datetime']
    content_url = 'https://news.cnyes.com/api/v6/news/' + id
    content_response = session.get(content_url, headers = headers)
    content_json = content_response.json()
    content = content_json['items']['content']
    tag = content_json['items']['keywords']
    href = 'https://news.cnyes.com' + article_id
    output = {'date': date, 'title': title, 'content': content, 'href': href, 'tag': tag, 'clicks': 'NA'}
    time.sleep(1)
    if not os.path.exists(path %(title)):
        with open(path %(title) + '.json', 'w', encoding='utf8') as f:
            json.dump(output,f)
session.close()
