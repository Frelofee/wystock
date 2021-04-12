# 王琰的python编写
# 开发时间:2021/3/27 10:49

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

# 找到输入框 （kw后面会具体解释，还有下面具体的标签）
shuru = Edge_driver.find_element_by_id('kw')
# 在输入框中放我们制定的文字
shuru.send_keys('网易云音乐')
#为了我们肉眼可见，这里休眠2秒，再进行下面的操作
time.sleep(2)

# 找到百度一下按钮
sousuo = Edge_driver.find_element_by_id('su')
# 点击某个对象（点击百度一下）
sousuo.click()
time.sleep(2)

#找到网易云音乐
# wangyi = Edge_driver.find_element_by_id('1').find_element_by_tag_name('a')
# print(wangyi)

# 方法1根据id直接填入值
Edge_driver.execute_script("document.getElementById('kw').value ='halihali'")
# def setAttribute(Edge_driver, elementObj, attributeName, value):
#     # 更改元素的属性的值
#     Edge_driver.execute_script("arguments[0].setAttribute(arguments[1],arguments[2])", elementObj, attributeName, value)
# element = Edge_driver.find_element_by_id('kw')
# setAttribute(Edge_driver,element,'value','abcde') #更改元素的属性值
sousuo.click()

# 获取网页内容
context = Edge_driver.find_element_by_id('1').text
# context_q = context.get_attribute()
print(context)

# # 获取网页内容
# html_source = Edge_driver.page_source
# # 重点
# html = lxml.html.fromstring(html_source)
# # 获取标签下所有文本
# items = html.xpath("//div[@id='y_prodsingle']//text()")
# # 正则 匹配以下内容 \s+ 首空格 \s+$ 尾空格 \n 换行
# pattern = re.compile("^\s+|\s+$|\n")
#
# clause_text = ""
# for item in items:
#     # 将匹配到的内容用空替换，即去除匹配的内容，只留下文本
#     line = re.sub(pattern, "", item)
#     if len(line) > 0:
#         clause_text += line + "\n"
# #
# #
# print(clause_text)

