# 王琰的python编写
# 开发时间:2021/3/24 8:57

import os
import pandas as pd
import PyQt5
def get_files(path):
    fs=[]
    for root,dirs,files in os.walk(path):
        for file in files:
            fs.append(os.path.join(root,file))
    return fs

def merge():
    files=get_files('D:/我的成长/2021开心的我/工作/局内工作/社保工作/社保/死亡/2020年死因')
    df=pd.DataFrame()
    for i in files:
        #print(i)
        df1=pd.read_excel(i)
        #print(df1)
        df=pd.concat([df,df1],axis=0)
    df.to_excel('D:/我的成长/2020无敌的我/我的生活：保持良好状态，陶冶生活情操/python学习/素材/test/merge.xlsx',index=False)

if __name__=='__main__':
    merge()
