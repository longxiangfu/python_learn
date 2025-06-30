"""
利用selenium自动化检测gitHub项目
1、准备:利用selenuum打开百度
"""
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

# 创建Service对象并指定ChromeDriver的路径
service = Service(executable_path='chromedriver.exe')

# 初始化WebDriver，并传入service参数
driver = webdriver.Chrome(service=service)
# 打开百度
driver.get('https://www.baidu.com')
# 获取页面元素：输入框
input = driver.find_element('id', 'kw')
# 清空输入框
input.clear()
# 输入内容
input.send_keys('CSDN')
# 回车
input.send_keys(Keys.ENTER)

time.sleep(5)
input.clear()
input.send_keys('java')
input.send_keys(Keys.ENTER)

# 等待60s
time.sleep(60)