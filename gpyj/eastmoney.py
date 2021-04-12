# 王琰的python编写
# 开发时间:2021/4/12 9:34
import time
from selenium import webdriver
import lxml
import re

driver = "C:/Program Files (x86)/Microsoft/Edge/Application/msedgedriver.exe"
Edge_driver = webdriver.Edge(driver)

url = "http://quote.eastmoney.com/center/gridlist.html#hs_a_board/"
Edge_driver.get(url)

#最大化窗口（默认不是最大化）
Edge_driver.maximize_window()

# 找到标签
context_ct = Edge_driver.find_element_by_id('table_wrapper-table').text
print(context_ct)
context_num = Edge_driver.find_element_by_class_name('paginate_page').text
print(context_num)
context_Num = re.findall('…(.*)',context_num)
print(context_Num)
Num = int(context_Num[0])
for i in range(1,Num):
    print(i)

