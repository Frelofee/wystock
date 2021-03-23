# 王琰的python编写
# 开发时间:2021/3/22 9:46

import baostock as bs
import pandas as pd
from datetime import datetime
from itertools import chain

# 登陆系统
lg = bs.login()
# 显示登陆返回信息
print('login respond error_code:'+lg.error_code)
print('login respond  error_msg:'+lg.error_msg)

# 获取指数(综合指数、规模指数、一级行业指数、二级行业指数、策略指数、成长指数、价值指数、主题指数)K线数据
# 综合指数，例如：sh.000001 上证指数，sz.399106 深证综指 等；
# 规模指数，例如：sh.000016 上证50，sh.000300 沪深300，sh.000905 中证500，sz.399001 深证成指等；
# 一级行业指数，例如：sh.000037 上证医药，sz.399433 国证交运 等；
# 二级行业指数，例如：sh.000952 300地产，sz.399951 300银行 等；
# 策略指数，例如：sh.000050 50等权，sh.000982 500等权 等；
# 成长指数，例如：sz.399376 小盘成长 等；
# 价值指数，例如：sh.000029 180价值 等；
# 主题指数，例如：sh.000015 红利指数，sh.000063 上证周期 等；


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
result1.drop([i for i in range(0,4720)],inplace=True)

# dataframe columns to list
rlist = result1.code.values.tolist()
# 求数组长度 rnum = len(rlist)
data_list = []
# 遍历list
for r in rlist:
	rs = bs.query_history_k_data_plus(r,
	    "date,code,open,high,low,close,preclose,volume,amount,adjustflag,turn,tradestatus,pctChg,peTTM,pbMRQ,psTTM,pcfNcfTTM,isST",
	    start_date='2021-01-11', end_date='2021-03-19',
	    frequency="d", adjustflag="3") #frequency="d"取日k线，adjustflag="3"默认不复权
	print('query_history_k_data_plus respond error_code:{}, error_msg:{}'.format(rs.error_code, rs.error_msg))
	#### 打印结果集 ####
	while (rs.error_code == '0') & rs.next():
	    # 获取一条记录，将记录添加到data_list
	    data_list.append(rs.get_row_data())


# list转化pd
result = pd.DataFrame(data_list, columns=rs.fields)

# 求5日均线的值
# 转换数据类型
result = result.astype({'close': float})
print(result)
# result = result.astype({'amount': float})

# 设置列表存储数据
close_s = []
close_c = []
# code固定情况下，定义时间
date_list = result.loc[0:5,'date']
sum_date = date_list.sum()

# 方法1：根据某个固定code与时间的，5日线求和函数
# def total_5(Th):
#     # Th = result[result['date'].isin(['2019-01-08'])].index.values 例子.根据日期得到所在行
#     # Th = result[result['date'].isin([rdate])].index.values
#     # print(Th[0])
#     date_close = []
#
#     for i in range(5):
#         date_close.append(result.loc[(Th-i),'close'])
#         print(date_close)
#     date_c = pd.DataFrame(date_close,index=[0,1,2,3,4])
#     print(date_c)
#     #print(date_c.loc[0,0])
#     total = 0.0
#     for i in range(len(date_close)):
#         total = total + date_c.loc[i,(Th-i)]
#         print(total)
#         # print(Th[0]+i)
#         i = i+1
#         # 收盘价close的百分比
#     # total为5日close总和
#     print(total)
#     return total

# 方法2：根据某个固定code与时间的，5日线求和函数
def total_5(Th):
    # Th = result[result['date'].isin(['2019-01-08'])].index.values 例子.根据日期得到所在行
    # Th = result[result['date'].isin([rdate])].index.values
    # print(Th[0])
    date_close = []
    for i in range(5):
        date_close.append(result.loc[(Th-i),'close'])
        print(date_close)
    date_c = pd.DataFrame(date_close,index=[0,1,2,3,4])
    print(date_c)
    #print(date_c.loc[0,0])
    total = 0.0
    for i in range(len(date_close)):
        total = total + date_close[i]
        print(total)
        i = i+1
        # 收盘价close的百分比
    # total为5日close总和
    total5 = total/5
    print(total/5)
    return total5

# 方法2：根据某个固定code与时间的，60日线求和函数
def total_60(Th):
    # Th = result[result['date'].isin(['2019-01-08'])].index.values 例子.根据日期得到所在行
    # Th = result[result['date'].isin([rdate])].index.values
    # print(Th[0])
    date_close = []
    for i in range(60):
        date_close.append(result.loc[(Th-i),'close'])
        print(date_close)
    date_c = pd.DataFrame(date_close,index=['0:59'])
    print(date_c)
    #print(date_c.loc[0,0])
    total = 0.0
    for i in range(len(date_close)):
        total = total + date_close[i]
        print(total)
        i = i+1
        # 收盘价close的百分比
    # total为5日close总和
    total5 = total/60
    print(total/60)
    return total5

# code的不重复名单
close_s = result.groupby(by='code')['close'].sum()
sum_close = sum(result['close'])
rowVal = []
for i in range(len(close_s)):
    rowValArray = []
    rowValArray.append('')
    rowValArray.append(close_s.iloc[i])
    rowVal.append(rowValArray)
# 生成close_S是close求和后的汇总表
close_S = pd.DataFrame(rowVal, columns=['code', 'close'])
close_S['code'] = result['code'].unique()
print(close_S)

Sh = close_S['code']
yq = []
list_5 = []
list_60 = []
for r in Sh:
    # 根据code，求出code在close_S中的所在行
    result_date = result[result['code'].isin([r])].index.values
    time_list = result_date.tolist()
    print(time_list)

    for t in time_list:
        p = time_list.index(t)
        if(p >= 4):
            print(t)
            list_5.append(total_5(t))
        else:
            list_5.append('0')
            continue
    print(list_5)
result['5rx'] = list_5

for r in Sh:
    # 根据code，求出code在close_S中的所在行
    result_date = result[result['code'].isin([r])].index.values
    time_list = result_date.tolist()
    print(time_list)

    for t in time_list:
        p = time_list.index(t)
        if (p >= 59):
            print(t)
            list_60.append(total_60(t))
        else:
            list_60.append('0')
            continue
    print(list_60)
result['60rx'] = list_60

for r in Sh:
    yq_5 = [0]
    result_date = result[result['code'].isin([r])].index.values
    time_list = result_date.tolist()
    print(time_list)
    for i in time_list[1:]:
        print(result.columns.values)
        close_50 = result.iloc[(i-1),[-1]]
        close_50 = float(close_50)
        close_51 = result.iloc[i,[-1]]
        close_51 = float(close_51)
        close_52 = close_51+close_51 - close_50
        close_52 = float(close_52)
        if(close_52 < close_51):
            yq_5.append('1')
        else:
            yq_5.append('0')
            continue
    yq.append(yq_5)
    print(yq)
    # 多维数组转一维数组
yq = list(chain.from_iterable(yq))
result['5yq'] = yq

# 结果集输出到csv文件
result.to_csv("D:/我的成长/2021开心的我/生活/股票池/5日线x.csv", index=False)
print(result)

# 登出系统
bs.logout()