# 王琰的python编写
# 开发时间:2021/4/12 16:14

import time
from selenium import webdriver
import lxml
import re

driver = "C:/Program Files (x86)/Microsoft/Edge/Application/msedgedriver.exe"
Edge_driver = webdriver.Edge(driver)

url = "https://www.damai.cn/"
Edge_driver.get(url)

# 登入
Login_1 = Edge_driver.find_element_by_class_name('user-header')
Login_1.click()

# 登入Frame
Edge_driver.switch_to.frame('alibaba-login-box')
Id = Edge_driver.find_element_by_id('fm-login-id')
Secret = Edge_driver.find_element_by_id('fm-login-password')
Submit = Edge_driver.find_element_by_class_name('fm-btn')
print(Edge_driver.current_url)
Id.send_keys('')# 账号
time.sleep(2)
Secret.send_keys('')# 密码
time.sleep(1)
Submit.click()
print(Edge_driver.current_url)
time.sleep(2)

tag_tk = Edge_driver.find_element_by_class_name('input-search')
# 要抢票的项目
tag_tk.send_keys('2021武汉草莓音乐节')
Edge_driver.find_element_by_class_name('btn-search').click()
tag_tk0 = Edge_driver.find_element_by_link_text('2021武汉草莓音乐节')
tag_tk0.click()

# 到新页面
windows_after = Edge_driver.window_handles[1]
Edge_driver.switch_to.window(windows_after)
url1 = Edge_driver.current_url
print(url1)

# 知道了
Edge_driver.find_element_by_link_text('知道了').click()
Edge_driver.find_element_by_xpath('//span[text()="2021-05-02 周日 13:00"]').click()
Edge_driver.find_element_by_xpath('//span[text()="预售单日票 360元"]').click()

