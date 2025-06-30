"""
利用selenium自动化检测gitHub项目是否更新
2、检测
"""

import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

name = 'psf/requests'
api = 'https://api.github.com/repos/' + name
weburl = 'https://github.com/' + name


old_time = None
while True:
    r = requests.get(api)
    if r.status_code != 200:
        print('请求api失败')
        break

    print('请求api成功')
    convert = r.json()  # 返回的为字典类型dict(json响应转成python对象)
    print('convert:', convert)
    now_time = convert['updated_at']
    print('not old_time:', not old_time)
    if not old_time:
        old_time = now_time

    # requests库有更新的话，则打开网址
    if old_time >= now_time:
        driver = webdriver.Chrome(service=Service(executable_path='chromedriver.exe'))
        print('打开网址https://github.com/psf/requests')
        driver.get(weburl)

    time.sleep(1)