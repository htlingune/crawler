import json
import re
import os
path = r''
files = os.listdir(path)
error_title = []
for file in files:
    try:
        with open(path+'%s'% (file), 'r', encoding='utf-8') as f:
            for line in f.readlines():
                dic = json.loads(line)
                content = dic['content']
                if re.search(r'(<a.+?a>)', content) != None:
                    content = re.sub(r"(\(<a.+?a>\))", '', content, count=0, flags=re.IGNORECASE)
                if re.search(r'(\n)', content) != None:
                    content = re.sub(r'(\n)', '', content, count=0)
                if re.search(r'(&l.+?gt;)', content) != None:
                    content = re.sub(r'(&l.+?gt;)', '', content, count=0)
                if re.search(r'(&a.+?sp;)', content) != None:
                    content = re.sub(r'(&a.+?sp;)', '', content, count=0)
                dic['content'] = content
        with open(path+'%s'% (file), 'w', encoding='utf-8') as f:
            json.dump(dic, f)
    except :
        error_title.append(file)
print(error_title)
