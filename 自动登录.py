# 王琰的python编写
# 开发时间:2021/3/27 10:49

import time
from selenium import webdriver


driver = "C:/Program Files (x86)/Microsoft/Edge/Application/msedgedriver.exe"
Edge_driver = webdriver.Edge(driver)

url = "https://www.baidu.com/"
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

# 方法1js
Edge_driver.execute_script("document.getElementById('kw').value ='halihali'")
# def setAttribute(Edge_driver, elementObj, attributeName, value):
#     # 更改元素的属性的值
#     Edge_driver.execute_script("arguments[0].setAttribute(arguments[1],arguments[2])", elementObj, attributeName, value)
# element = Edge_driver.find_element_by_id('kw')
# setAttribute(Edge_driver,element,'value','abcde') #更改元素的属性值
sousuo.click()
# Edge_driver.refresh()

# 方法2键盘操作