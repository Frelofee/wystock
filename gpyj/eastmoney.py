# 王琰的python编写
# 开发时间:2021/4/12 9:34
import time
from selenium import webdriver
import lxml
import re
import pandas as pd

driver = "C:/Program Files (x86)/Microsoft/Edge/Application/msedgedriver.exe"
Edge_driver = webdriver.Edge(driver)

url = "http://quote.eastmoney.com/center/gridlist.html#hs_a_board/"
Edge_driver.get(url)

#最大化窗口（默认不是最大化）
Edge_driver.maximize_window()

# 找到股票信息标签
context_ct = Edge_driver.find_element_by_id('table_wrapper-table').text

# 找到页面标签
context_num = Edge_driver.find_element_by_class_name('paginate_page').text
print(context_num)
# 定制页面跳转循环
context_Num = re.findall('…(.*)',context_num)
print(context_Num)
Num = int(context_Num[0])
context_Ct = []
for i in range(1,Num):
    context_ct = Edge_driver.find_element_by_id('table_wrapper-table').text
    print(context_ct)
    print('Page.'+str(i)+'页打印成功')
    context_Ct.append(context_ct)
    # 点击跳转按钮标签
    Edge_driver.find_elements_by_xpath('//a[text()="下一页"]')[0].click()
    time.sleep(0.25)
result = pd.DataFrame(context_Ct)
result.to_csv("D:/我的成长/2021开心的我/生活/股票池/early.csv", index=False)




