"""
爬虫二。要爬取的内容在script内
"""

import re
import json
import pandas as pd
import requests


url = "https://ncov.dxy.cn/ncovh5/view/pneumonia"

# 爬取的内容即html
page = requests.get(url).content.decode("utf-8")

# 目标内容的正则表达式
regexp = "<script id=\"getAreaStat\">([^<]+)"

# 找到目标内容
res = re.findall(regexp, page)
print(res)
data = res[0][27:-11]
print(data)
# 转成json类型
lst = json.loads(data)
for dic in lst:
    print(dic)

# 生成DataFrame对象
df = pd.DataFrame(lst)
# 将数据以追加的形式写到csv文件中
df.to_csv("ncov.csv", mode="a")



