# 王琰的python编写
# 开发时间:2021/3/3 19:04
import baostock as bs
import pandas as pd

#### 登陆系统 ####
lg = bs.login()
# 显示登陆返回信息
print('login respond error_code:'+lg.error_code)
print('login respond  error_msg:'+lg.error_msg)

#### 获取历史K线数据 ####
# 详细指标参数，参见“历史行情指标参数”章节
cd = bs.query_all_stock(day="2017-06-30")
cd_list = []
while (cd.error_code == '0') & cd.next():
    # 获取一条记录，将记录合并在一起
    cd_list.append(cd.get_row_data())
result1 = pd.DataFrame(cd_list, columns=cd.fields)
print(result1)

# dataframe columns to list
rlist = result1.code.values.tolist()
data_list = []
# 遍历list
for r in rlist:
	rs = bs.query_history_k_data_plus(r,
	    "date,code,open,high,low,close,preclose,volume,amount,adjustflag,turn,tradestatus,pctChg,peTTM,pbMRQ,psTTM,pcfNcfTTM,isST",
	    start_date='2020-01-01', end_date='2021-03-05',
	    frequency="d", adjustflag="3") #frequency="d"取日k线，adjustflag="3"默认不复权
	print('query_history_k_data_plus respond error_code:{}, error_msg:{}'.format(rs.error_code, rs.error_msg))
	#### 打印结果集 ####
	while (rs.error_code == '0') & rs.next():
	    # 获取一条记录，将记录添加到data_list
	    data_list.append(rs.get_row_data())

# list转化pd
result = pd.DataFrame(data_list, columns=rs.fields)
#### 结果集输出到csv文件 ####
result.to_csv("D:/history.csv", encoding="gbk", index=False)
print(result)

#### 登出系统 ####
bs.logout()