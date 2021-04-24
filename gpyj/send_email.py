# 王琰的python编写
# 开发时间:2021/4/23 15:16

import smtplib
from email.mime.text import MIMEText
from email.header import Header
# login
smtp_obj = smtplib.SMTP_SSL("smtp.qq.com",465,"utf-8")
# smtp_obj.login("631538973@qq.com","ovfdnymnitlabdcb")# pop3
smtp_obj.login("631538973@qq.com","mmwylzpetumebffh")# imap
# set email message
msg = MIMEText("这是一条成功的道路")
msg["From"] = Header("财富密码","utf-8")
msg["To"] = Header("我的财富密码","utf-8")
msg["Subject"] = Header("超级财富","utf-8")

# send email
smtp_obj.sendmail("631538973@qq.com","631538973@qq.com",msg.as_string())