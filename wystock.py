# encoding:utf-8
# 王琰的python编写
# 开发时间:2021/3/3 19:04
import baostock as bs
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from itertools import chain


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
#result1.drop([i for i in range(0,4700)],inplace=True)

# dataframe columns to list
rlist = result1.code.values.tolist()
# 求数组长度 rnum = len(rlist)
data_list = []
# 遍历list
for r in rlist:
	rs = bs.query_history_k_data_plus(r,
	    "date,code,open,high,low,close,preclose,volume,amount,adjustflag,turn,tradestatus,pctChg,peTTM,pbMRQ,psTTM,pcfNcfTTM,isST",
	    start_date='2021-03-15', end_date='2021-03-19',
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
result = result.astype({'close':float})
result = result.astype({'amount':float})
print((result['close'].dtypes))

# 设置列表存储数据
close_s = []
# 收盘价close的百分比
close_s = result.groupby(by='code')['close'].sum()
sum_close = sum(result['close'])
rowVal = []
for i in range(len(close_s)):
    rowValArray = []
    rowValArray.append('')
    rowValArray.append(close_s.iloc[i])
    rowVal.append(rowValArray)
# 生成close_S是close求和后的汇总表
close_S = pd.DataFrame(rowVal,columns=['code','close'])
close_S['code'] = result['code'].unique()

# 设置列表存储数据
amount_s = []
# 成交金额amount的百分比
amount_s = result.groupby(by='code')['amount'].sum()
sum_amount = sum(result['amount'])
rowAal = []
for i in range(len(amount_s)):
    rowAalArray = []
    rowAalArray.append((''))
    rowAalArray.append((amount_s.iloc[i]))
    rowAal.append(rowAalArray)
# 生成amount_S是amount求和后的汇总表
amount_S = pd.DataFrame(rowAal,columns=['code','amount'])
amount_S['code'] = result['code'].unique()
# print(close_S.loc['1',['code']])
# print(sum_close)
# print(close_S)
# print(close_S.dtypes)

# 遍历得到各组数据的百分比成长值
# print(len(result))
# print(list(range(len(result))))
# 例子
# df取值：print(close_S.loc[['sz.399914'],['close']])
# 找出'sz.399914'对应行：result_a = result[result['code'].isin(['sz.399914'])].index.values
# df取值print(result.loc[[0],['code']])
# close_Sh = close_S[close_S['code'].isin(['sz.399913'])].index.values
# print(close_Sh)
# 卧槽，我真牛逼，这里要close_Sh要用元组，不能用列表
# print(close_S.loc[(close_Sh),['close']])
# 列表取值：print(close_s[2])
# 测试除法：print(1/2)
# 设置列表存储数据
Sh = close_S['code']
result_css = []
for r in Sh:
    # 根据code，求出code在close_S中的所在行
    close_Sh = close_S[close_S['code'].isin([r])].index.values
    # 根据所在行，求出code对应的close总和
    close_Shh = close_S.loc[(close_Sh),('close')]
    # 求出code在原表中的所在行
    result_a = result[result['code'].isin([r])].index.values
    result_cs = []
    result_dates = []
    for r in result_a:
        result_c = result.loc[r,['close']]
        result_c = float(result_c)
        result_cc = result_c/close_Shh
        result_cs.append(float(result_cc))
        result_dates.append("{}".format(result.loc[r, ['date']]['date']))
    print(result_dates)
    print(result_cs)
    # 作图
    plt.plot(result_dates, result_cs, label=close_S.loc[(close_Sh),('code')])
    # 生成总的百分比表
    result_css.append(result_cs)
# 多维数组转一维数组
result_csS = list(chain.from_iterable(result_css))
# 定位图例位置
plt.legend(loc=2, bbox_to_anchor=(1.02,1.0), borderaxespad=0.1, ncol=1)

Ah = amount_S['code']
result_ass = []
for r in Sh:
    # 根据code，求出code在close_S中的所在行
    amount_Sh = amount_S[amount_S['code'].isin([r])].index.values
    # 根据所在行，求出code对应的close总和
    amount_Shh = amount_S.loc[(amount_Sh), ('amount')]
    # 求出code在原表中的所在行
    amount_a = result[result['code'].isin([r])].index.values
    amount_cs = []
    amount_dates = []
    for r in amount_a:
        amount_c = result.loc[r, ['amount']]
        amount_c = float(amount_c)
        amount_cc = amount_c / amount_Shh
        amount_cs.append(float(amount_cc))
        amount_dates.append("{}".format(result.loc[r, ['date']]['date']))
    print(amount_dates)
    print(amount_cs)
    # 作图
    #plt.plot(amount_dates, amount_cs, label=close_S.loc[(amount_Sh), ('code')])
    # 生成总的百分比表
    result_ass.append(amount_cs)
    # 多维数组转一维数组
result_asS = list(chain.from_iterable(result_ass))

#plt.legend(loc=2, bbox_to_anchor=(1.02, 1.0), borderaxespad=0.1, ncol=1)
#plt.savefig('D:/我的成长/2021开心的我/生活/股票池/stock.svg')

# 添加到后面
result['newclose'] = result_csS
result['newamount'] = result_asS

#### 结果集输出到csv文件 ####
result.to_csv("D:/我的成长/2021开心的我/生活/股票池/test6.csv", encoding="gbk", index=False)
# 输出图表
#plt.show()


#### 登出系统 ####
bs.logout()