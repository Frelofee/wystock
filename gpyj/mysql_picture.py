# 王琰的python编写
# 开发时间:2021/5/13 20:14
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
import pandas as pd

# 创建连接
conn = create_engine('mysql+pymysql://root:wy123456@localhost:3306/mysql?charset=utf8')
# 读取数据库表
data = pd.read_sql("select CAST(SUBSTRING(DT_DATE,9,2) AS SIGNED) DT_DATE,HIGH_TEMP,LOW_TEMP from tb",con=conn)