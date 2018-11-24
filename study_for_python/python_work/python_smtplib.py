import smtplib
from email.mime.text import MIMEText

from_mail = "json_hc@163.com"  # 发件人
to_mail = "346165580@qq.com"  # 收件人
mail_passwd = "HHq123456"  # 163邮件的授权码而不是登录密码

content = "this is the first python email"   # 邮件正文
subject = "mail test"   # 主题
msg = MIMEText(content)
msg['Subject'] = subject
msg['From'] = from_mail
msg['To'] = to_mail
try:
    s = smtplib.SMTP()    # 创建SMTP对象
    s.connect('smtp.163.com')  # 连接到smtp服务器
    s.login(from_mail, mail_passwd)  # 登录163邮箱
    s.sendmail(from_mail, to_mail, msg.as_string())  # 使用smtp服务器向外发送邮件
    print("OK")
except Exception as e:
    print(e)
finally:
    s.quit()
