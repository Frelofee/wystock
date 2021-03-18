# 王琰的python编写
# 开发时间:2021/3/3 19:04
import baostock as bs
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter

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
# 遍历list
for r in rlist:
	rs = bs.query_history_k_data_plus(r,
	    "date,code,open,high,low,close,preclose,volume,amount,adjustflag,turn,tradestatus,pctChg,peTTM,pbMRQ,psTTM,pcfNcfTTM,isST",
	    start_date='2021-03-04', end_date='2021-03-05',
	    frequency="d", adjustflag="3") #frequency="d"取日k线，adjustflag="3"默认不复权
	print('query_history_k_data_plus respond error_code:{}, error_msg:{}'.format(rs.error_code, rs.error_msg))
	#### 打印结果集 ####
	while (rs.error_code == '0') & rs.next():
	    # 获取一条记录，将记录添加到data_list
	    data_list.append(rs.get_row_data())



# list转化pd
result = pd.DataFrame(data_list, columns=rs.fields)

# 转换数据类型
print(result)
print(result.dtypes)
result= result.astype({'close':float})
print((result['close'].dtypes))

# 设置列表存储数据
close_s = []
# 求和
close_s = result.groupby(by='code')['close'].sum()
sum_close = sum(result['close'])
close_S = pd.DataFrame(close_s,columns=['code','close'])
close_S['code'] = result['code'].unique()
print(close_s)
print(sum_close)
print(close_S)
print(close_S.dtypes)

# 遍历得到各组数据的百分比成长值
print(len(result))
print(list(range(len(result))))
Sh = close_S.index.values
# 例子
# df取值：print(close_S.loc[['sz.399914'],['close']])
# 找出'sz.399914'对应行：result_a = result[result['code'].isin(['sz.399914'])].index.values
# df取值print(result.loc[[0],['code']])
# close_Sh = close_S[close_S['code'].isin(['sz.399914'])].index.values
# print(close_Sh)
# 卧槽，我真牛逼，这里要close_Sh要用元组，不能用列表
# print(close_S.loc[(close_Sh),['close']])
# 列表取值：print(close_s[2])
# 测试除法：print(1/2)
# 设置列表存储数据
result_cs = []
for r in Sh:
    close_Sh = close_S[close_S['code'].isin([r])].index.values
    close_Shh = close_S.loc[(close_Sh),['close']]
    result_a = result[result['code'].isin([r])].index.values
    for r in result_a:
        result_c = result.loc[r,['close']]
        result_c = float(result_c)
        result_cc = result_c/close_Shh
        result_cs.append(result_cc)

print(result_cs.index)
print(result_cs)
#for result_cs_Element in result_cs:
#    print(type(result_cs_Element))
#result_css = pd.DataFrame(result_cs).set_index('code')
#print(result_css)
#result['new'] = result_cs
#print(result_css)
#图表输出
#result_cs.plot
#plt.show()


#### 结果集输出到csv文件 ####
#result.to_csv("D:/我的成长/2021开心的我/生活/股票池/test2.csv", encoding="gbk", index=False)

#对数据转图表前，进行加工
#result.drop([i for i in range(len(ls)-1)],inplace=True)
#print(result)

#输出图表？
#result.plot((result.date.value), result.open, data=result)
#plt.show()

#### 登出系统 ####
bs.logout()