"""
利用selenium自动化检测gitHub项目
1、准备:利用selenuum打开百度
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get('https://www.baidu.com')
input = driver.find_element_by_id('kw')
input.clear()
input.send_keys('CSDN')
input.send_keys(Keys.ENTER)