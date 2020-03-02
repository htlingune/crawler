import json
import re
import os
path = ''
files = os.listdir(path)
error_title = []
for file in files:
    try:
        with open(path+'%s'% (file), 'r', encoding='utf-8') as f:
            for line in f.readlines():
                dic = json.loads(line)
                content = dic['content']
                if re.search('不用抽',content).start() != None:
                    stop_index = re.search('不用抽',content).start()
                    content = content[:stop_index]
                if re.search(r'(\n)', content) != None:
                    content = content.replace('\r', '')
                    content = content.replace('\n', '')
                    content = content.replace(' ', '')
                dic['content'] = content
        with open(path+'%s'% (file), 'w', encoding='utf-8') as f:
            json.dump(dic, f)
    except :
        error_title.append(file)
print(error_title)