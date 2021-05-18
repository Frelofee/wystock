# 王琰的python编写
# 开发时间:2021/5/8 16:38

import numpy as np

def sumpy():
    a = np.array([0,1,2,3,4,5])
    b = np.array([5,6,7,8,9,10])
    c = a**2 + b**3
    return c
print(sumpy())