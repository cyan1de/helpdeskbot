import smtplib
from email.mime.text import MIMEText
from email.header import Header

mail_sender=''
mail_receiver=''
user_name=''
password=''
server = smtplib.SMTP_SSL('smtp.yandex.ru:465')
#server.login('user_name', 'password')


subject = u'Тестовый email от ' + mail_sender
body = u'Это тестовое письмо оптправлено '
msg = MIMEText(body, 'plain', 'utf-8')
msg['Subject'] = Header(subject, 'utf-8')

server.set_debuglevel(1);
server.ehlo()
server.login(user_name, password)
server.sendmail(mail_sender, mail_receiver, msg.as_string())
server.quit()