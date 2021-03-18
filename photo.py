# 王琰的python编写
# 开发时间:2021/3/10 19:29

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import baostock as bs
import pandas as pd
from openpyxl import *
#### 登陆系统 ####
lg = bs.login()
# 显示登陆返回信息
print('login respond error_code:'+lg.error_code)
print('login respond  error_msg:'+lg.error_msg)

#### 获取历史K线数据 ####
# 详细指标参数，参见“历史行情指标参数”章节
cd = bs.query_all_stock(day="2021-03-15")
cd_list = []
while (cd.error_code == '0') & cd.next():
    # 获取一条记录，将记录合并在一起
    cd_list.append(cd.get_row_data())
result1 = pd.DataFrame(cd_list, columns=cd.fields)
print(result1)

# 结果切片
result1.drop([i for i in range(0,4700)],inplace=True)

# dataframe columns to list
rlist = result1.code.values.tolist()
# 求数组长度 rnum = len(rlist)
data_list = []
for r in rlist:
	rs = bs.query_history_k_data_plus(r,
	    "date,code,open,high,low,close,preclose,volume,amount,adjustflag,turn,tradestatus,pctChg,peTTM,pbMRQ,psTTM,pcfNcfTTM,isST",
	    start_date='2021-03-04', end_date='2021-03-05',
	    frequency="d", adjustflag="3") #frequency="d"取日k线，adjustflag="3"默认不复权
	print('query_history_k_data_plus respond error_code:{}, error_msg:{}'.format(rs.error_code, rs.error_msg))
while (cd.error_code == '0') & cd.next():
    # 获取一条记录，将记录合并在一起
    cd_list.append(cd.get_row_data())
result1 = pd.DataFrame(cd_list, columns=cd.fields)
print(result1)
result1.drop([i for i in range(0,4700)],inplace=True)
print(result1)
#result1 = result1.drop(’code_name‘,axis=1)
del result1['code_name']
print(result1)

#### 转换数据型 ####
result1 = result1['tradeStatus'].astype(float)
#### 生成图表 ####
result1.plot(kind='bar')
plt.show()

