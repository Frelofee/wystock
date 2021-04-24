# 王琰的python编写
# 开发时间:2021/4/24 10:36
from datetime import datetime

star_time = datetime.now()
print('{}-{} {}:{}'.format(star_time.month,star_time.day,star_time.hour,star_time.minute))
print(star_time)