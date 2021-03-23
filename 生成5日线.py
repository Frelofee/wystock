# 王琰的python编写
# 开发时间:2021/3/22 9:46

import baostock as bs
import pandas as pd
from datetime import datetime

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


# 详细指标参数，参见“历史行情指标参数”章节；“周月线”参数与“日线”参数不同。
# 周月线指标：date,code,open,high,low,close,volume,amount,adjustflag,turn,pctChg
rs = bs.query_history_k_data_plus("sh.000002",
    "date,code,open,high,low,close,preclose,volume,amount,pctChg",
    start_date='2019-01-01', end_date='2019-06-30', frequency="d")
print('query_history_k_data_plus respond error_code:'+rs.error_code)
print('query_history_k_data_plus respond  error_msg:'+rs.error_msg)

# 打印结果集
data_list = []
while (rs.error_code == '0') & rs.next():
    # 获取一条记录，将记录合并在一起
    data_list.append(rs.get_row_data())
result = pd.DataFrame(data_list, columns=rs.fields)
'''
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
'''
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

#print(total_5('2019-01-05'))
close_c = result.groupby(by='code')['close'].sum()

#print(close_c)
#print(close_s)

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

# 根据code，求出code在close_S中的所在行
result_date = result[result['code'].isin(['sh.000002'])].index.values
time_list = result_date.tolist()
print(time_list)
list_5 = []
for t in time_list:
    p = time_list.index(t)
    if(p >= 4):
        print(t)
        list_5.append(total_5(t))
    else:
        list_5.append('0')
        continue
print(list_5)
result['5日线'] = list_5

# 结果集输出到csv文件
result.to_csv("D:/我的成长/2021开心的我/生活/股票池/5日线1.csv", index=False)
print(result)

# 登出系统
bs.logout()