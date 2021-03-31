# 王琰的python编写
# 开发时间:2021/3/26 13:20

#导入模块
import time
from selenium import webdriver

#实例化Chrome浏览器对象
edgedriver = "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe"
driver = webdriver.Ie(edgedriver)

#准备url
url='http://www.baidu.com'
# 访问
driver.get(url)
#最大化窗口（默认不是最大化）
driver.maximize_window()

# 找到输入框 （kw后面会具体解释，还有下面具体的标签）
shuru=driver.find_element_by_id('kw')
# 在输入框中放我们制定的文字
shuru.send_keys('网易云音乐')
#为了我们肉眼可见，这里休眠2秒，再进行下面的操作
time.sleep(2)

# 找到百度一下按钮
sousuo=driver.find_element_by_id('data-v-0b1f3c5b')
# 点击某个对象（点击百度一下）
sousuo.click()
time.sleep(2)

#找到网易云音乐
wangyi=driver.find_element_by_id('1').find_element_by_tag_name('a')
print(wangyi)
