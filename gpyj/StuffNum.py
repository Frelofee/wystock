# 王琰的python编写
# 开发时间:2021/4/17 23:24
import time
from selenium import webdriver
import lxml
import re

driver = "C:/Program Files (x86)/Microsoft/Edge/Application/msedgedriver.exe"
Edge_driver = webdriver.Edge(driver)

url = "http://www.iwencai.com/unifiedwap/home/stock/"
Edge_driver.get(url)

search_input = Edge_driver.find_element_by_xpath('//textarea[@class="search-input"]')
search_input.send_keys('601288历年员工人数')

search_click = Edge_driver.find_element_by_class_name('search-icon')
search_click.click()

# 这里是要的内容
context_ct = Edge_driver.find_element_by_class_name('jgy-table-wrapper').text
print(context_ct)

