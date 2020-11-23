"""
利用selenium自动化检测gitHub项目
2、检测
"""

import time
import requests
from selenium import webdriver



name = 'psf/requests'
api = 'https://api.github.com/repos/' + name
weburl = 'https://github.com' + name


old_time = None
while True:
    r = requests.get(api)
    if r.status_code != 200:
        print('请求api失败')
        break

    convert = r.json()  # 返回的为字典类型dict
    now_time = convert['updated_at']
    if not old_time:
        old_time = now_time

    if old_time < now_time:
        driver = webdriver.Chrome(executable_path='chromedriver.exe')
        driver.get(webdriver)

    time.sleep(5)