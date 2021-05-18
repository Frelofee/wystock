# 王琰的python编写
# 开发时间:2021/4/28 20:46

import cv2
from PIL import Image as ImagePIL
from PIL import Image
im = ImagePIL.open('D:/报名照片处理工具/报名照片/蔡琛.jpg')
print(im)
print(type(im))
# im = cv2.imread('D:/报名照片处理工具/报名照片/蔡琛.jpg')
# image = Image.fromarray(cv2.cvtColor(im,cv2.COLOR_BGR2RGB))
im.save('D:/报名照片处理工具/报名照片/蔡琛_bm.jpg',quality=95,dpi=(100.0,100.0))    #调整图像的分辨率