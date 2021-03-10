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
cd = bs.query_all_stock()
cd_list = []
while (cd.error_code == '0') & cd.next():
    # 获取一条记录，将记录合并在一起
    cd_list.append(cd.get_row_data())
result1 = pd.DataFrame(cd_list, columns=cd.fields)
print(result1)
result1 = result1.drop([0,4700],inplace=True)
print(result1)
result1 = result1.drop(’code_name‘,axis=1)
#del result1['code_name']

print(result1)

#esult1 = result1['tradeStatus'].astype(float)
result1.plot(kind='bar')
plt.show()

