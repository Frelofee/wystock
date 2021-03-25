# 王琰的python编写
# 开发时间:2021/3/25 12:47

import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

# FolderPath=filedialog.askdirectory()  #看情况自己使用
FilePath = filedialog.askopenfilenames()

# print('FolderPath:',FolderPath)
print('FilePath:',FilePath)

list_FilePath = []
list_FilePath = list(FilePath)
print(list_FilePath)

import os
import pandas as pd

def get_files(path):
    fs=[]
    for root,dirs,files in os.walk(path):
        for file in files:
            fs.append(os.path.join(root,file))
    return fs

def merge():
    # files = get_files('D:/我的成长/2020无敌的我/我的生活：保持良好状态，陶冶生活情操/python学习/素材/test')
    # print(files)
    df = pd.DataFrame()
    for i in list_FilePath:
        #print(i)
        df1=pd.read_excel(i)
        #print(df1)
        df=pd.concat([df,df1],axis=0)
    df.to_excel('D:/我的成长/2020无敌的我/我的生活：保持良好状态，陶冶生活情操/python学习/素材/test/merge.xlsx',index=False)

if __name__=='__main__':
    merge()

# for f in FilePath:
#     fo = f.split('.')[0]+'.csv'
#     with open(fo,'w') as foo:
#         with open(f,'r') as fn:
#             fn.readline()
#             for line in fn.readlines():
#                 li = line.strip().split()
#                 foo.write('%f,%f\n'%(float(li[1]),float(li[0])))
#                 print(li)
