# 王琰的python编写
# 开发时间:2021/4/22 9:48

from openpyxl import Workbook
from openpyxl import load_workbook
from pandas.io.excel import ExcelWriter
import pandas as pd

# 转格式
# pd.read_csv('D:/我的成长/2021开心的我/生活/股票池/early0422.csv').to_excel('D:/我的成长/2021开心的我/生活/股票池/early0422.xlsx')

# 实例化
wb = Workbook()
# active
ws = wb.active
# 直接读取excel工作簿
wb2 = load_workbook('D:/我的成长/2021开心的我/生活/股票池/early0422.xlsx')
print(wb2.sheetnames)
# 取工作表
sheet = wb2['Sheet1']
# 表最大行；最大列
max_row = sheet.max_row
print(max_row)
D = []
for m_row in range(max_row):
    # 读取单元格信息
    d = sheet.cell(row=m_row+1, column=2).value
    # print(d)
    d1 = d.split('\n')
    # print(d1)

    for i in range(len(d1)):
        i1 = str(d1[i])
        print(i1)
        d2 = i1.split(' ')
        print(d2)
        D.append(d2)
result = pd.DataFrame(D)
result.to_excel('D:/我的成长/2021开心的我/生活/股票池/test0424.xlsx')


