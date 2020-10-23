"""
爬虫一。要爬取的内容在html标签内
注意：python没有类型一说，变量可以引用任何类型，我们心里知道他是什么类型，然后再用相应的函数进行处理
"""

import requests
from lxml import html

# 要爬取的页面地址
url = "https://edu.csdn.net/course?cat2=348&payType=1&courseType=0&sort=1&cat1=280&page=1"

# 获取页面内容即html
page = requests.get(url).content.decode("utf-8")

# 将html转化为element/document
element = html.fromstring(page)

# 通过路径找到目标内容。注意xpath参数
titles = element.xpath("//body/div/div/div/div/div/div/div/div/div/div/div/div/div/div/a/text()")
for title in titles:
    print(title)
