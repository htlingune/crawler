import json
import os
dirpath = r'C:\Users\Big data\PycharmProjects\ETL\cnyesnewstoday'
files = os.listdir(dirpath)
tagset = set()
for file in files:
    try:
        with open(dirpath+'\\'+'%s'% (file), 'r', encoding='utf-8') as f:
            load_dict = json.load(f)
            tag_item = load_dict['tag']
            if len(tag_item) == 1:
                tagset.add(tag_item)
            if len(tag_item) > 1:
                tagset.update(tag_item)
    except Exception as e:
        print(e.args[0])
print(tagset)