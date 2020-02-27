import json
import pandas as pd

with open(r"filepath",'r',encoding= 'utf-8') as load_f:
    load_dict = json.load(load_f)
    print(load_dict)
	content = load_dict['content']
    content = re.sub(r"((<a)(.+?)(a>))",'',load_dict['content'],count=0)
    content = re.sub(r'(\\n)','',load_dict['content'],count=0)
    content = re.sub(r'(&l)(.+?)(gt;)','',load_dict['content'],count=0)
    print(content)
df = pd.read_json(r"filepath")

