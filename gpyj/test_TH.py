# 王琰的python编写
# 开发时间:2021/5/12 17:21
import time
import os
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import json
import requests
from requests.exceptions import RequestException
import re
from bs4 import BeautifulSoup
import csv
# from tqdm import tqdm
import pandas as pd
import os
os.getcwd() #获取当前工作路径

chrome_options = webdriver.ChromeOptions()
with open('xxxxx.js') as f:
    js = f.read()



time.sleep(2)
chrome_options.add_argument('user-agent="Mozilla/5.0 (iPod; U; CPU iPhone OS 2_1 like Mac OS X; ja-jp) AppleWebKit/525.18.1 (KHTML, like Gecko) Version/3.1.1 Mobile/5F137 Safari/525.20"')
chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
browser = webdriver.Chrome(options = chrome_options)
browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
  "source": js
})
browser.get('http://www.iwencai.com/unifiedwap/result?w=5g&querytype=&issugs')
WebDriverWait(browser,30,0.2).until(lambda x:x.find_element_by_css_selector("#app > div.wrapper > div > div.content.result_content > div.content_container > div > div.xuangu_container > div.xuangu_wrapper > div > div > div > div > div:nth-child(2) > div.jgy_tb_wrap > div > div.xuangu_showMore"))
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[1]/div[1]/div/div[1]/div[2]/div/div/div/div/div[2]/div[2]/div/div[3]').click()
n=input('随便输入一个信号：')#这里是手动滚动页面到底后的操作哭了
