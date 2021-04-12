# 王琰的python编写
# 开发时间:2021/4/4 12:26
# -*- coding:utf-8 -*-
import csv
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import matplotlib.ticker as ticker

from matplotlib.pyplot import MultipleLocator
from datetime import datetime
import pandas as pd

#将文本文件转换为cvs文件
#delimiter="\s+" 以空格作为分隔符
#df = pd.read_csv("D:\python39\my\data\procrank.txt",delimiter="\s+")
#df.to_csv("D:\python39\my\data\procrank.csv", encoding='utf-8', index=False)

filename = 'D:/我的成长/2021开心的我/生活/股票池/mouseshow/sitka_weather_2018_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    #print(header_row)
    texts,dates,highs,lows = [],[],[],[]
    for row in reader:
        # 将日期字符串转成日期对象
        current_date = datetime.strptime(row[2],'%Y/%m/%d')
        # 将日期对象设置为特定格式：format
        current_date1 = current_date.strftime('%Y/%m/%d')
        high = int(row[5])
        highs.append(high)
        low = int(row[6])
        lows.append(low)
        dates.append(current_date)
        texts.append(current_date1)
    print(current_date)

myfont = fm.FontProperties(fname=r'C:\Windows\Fonts\msyh.ttc')#设置字体
#根据最高温度绘制图形
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates,highs,c='red')
ax.plot(dates,lows, c='blue')

#设置图形格式
ax.set_title("2018年每日最高温度",fontproperties=myfont,fontsize=24)
ax.set_xlabel('',fontproperties=myfont,fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("温度（F）",fontproperties=myfont,fontsize=16)
ax.tick_params(axis='both',which='major',labelsize=16)

#设置图形格式：横坐标2018/01/01~2018/12/31，间隔为30；纵坐标0~70，间隔为5
ax.set_ylim(10, 80)
date_start = datetime(2017,12,28)
date_end = datetime(2019, 1, 3)
ax.set_xlim(date_start, date_end)
x_major_locator = MultipleLocator(30)
# 把x轴的刻度间隔设置为30，并存在变量里
y_major_locator = MultipleLocator(5)
# 把y轴的刻度间隔设置为5，并存在变量里
ax = plt.gca()
# ax为两条坐标轴的实例
ax.xaxis.set_major_locator(x_major_locator)
# 把x轴的主刻度设置为1的倍数
ax.yaxis.set_major_locator(y_major_locator)

#定义鼠标在最高温某点时显示的文本
text_high = []
for i in range(len(dates)):
    str_info = ("日期:%s \n最高温:%s ℃" %(texts[i],highs[i]))
    text_high.append(str_info)

    # 定义鼠标在最低温某点时显示的文本
text_low = []
for i in range(len(dates)):
    str_info = ("日期:%s \n最低温:%s ℃" % (texts[i], lows[i]))
    text_low.append(str_info)

# 定义最高温焦点属性
po_annotation_high,po_annotation_low= [],[]
for i in range(len(dates)):
    # 标注点的坐标
    point_x = dates[i]
    point_y1 = highs[i]
    point_y2 = lows[i]
    point_high, = plt.plot(point_x, point_y1, 'o', c='darkgreen',markersize=0)
    point_low, = plt.plot(point_x, point_y2, 'o', c='darkgreen', markersize=0)
    # 标注框偏移量
    offset1 = 15
    offset2 = 15
    # 标注框
    bbox1 = dict(boxstyle="round", fc='red', alpha=0.6)
    bbox2 = dict(boxstyle="round", fc='blue', alpha=0.3)
    # 标注箭头
    # arrowprops1 = dict(arrowstyle="->", connectionstyle="arc3,rad=0.")
    # 标注
    annotation_high = plt.annotate(text_high[i],xy=(dates[i], highs[i]), xytext=(-offset1, offset2), textcoords='offset points',
                                  bbox=bbox1, fontproperties=myfont, size=15)
    annotation_low = plt.annotate(text_low[i], xy=(dates[i], lows[i]), xytext=(15, -60), textcoords='offset points',
                              bbox=bbox2, fontproperties=myfont, size=15)
    # 默认鼠标未指向时不显示标注信息
    annotation_high.set_visible(False)
    annotation_low.set_visible(False)
    po_annotation_high.append([point_high, annotation_high])
    po_annotation_low.append([point_low, annotation_low])


# 定义鼠标响应函数
def on_move(event):
    visibility_changed = False
    for point, annotation in po_annotation_high:
        should_be_visible = (point.contains(event)[0] == True)

        if should_be_visible != annotation.get_visible():
            visibility_changed = True
            annotation.set_visible(should_be_visible)
    for point, annotation in po_annotation_low:
        should_be_visible = (point.contains(event)[0] == True)
        if should_be_visible != annotation.get_visible():
            visibility_changed = True
            annotation.set_visible(should_be_visible)
    if visibility_changed:
        plt.draw()


# 鼠标移动事件
on_move_id = fig.canvas.mpl_connect('motion_notify_event', on_move)
#plt.savefig('D:\python39\my\data\F.jpg')  # 保存为png格式
plt.show()
