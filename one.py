import smtplib
from email.mime.text import MIMEText
import re
from bs4 import BeautifulSoup
import requests
from email.utils import formataddr
my_sender = "369212851@qq.com"
my_pwd = "tkkterceepmhbigi"
receiver = ["2662997430@qq.com",
            '1632133690@qq.com',
            '369212851@qq.com',
            '1030664373@qq.com',
            '2215512468@qq.com',
            '1499138132@qq.com']


def spider():
    list = []
    response = requests.get('http://wufazhuce.com/')
    html = response.text
    html = BeautifulSoup(html, 'html.parser')
    content = html.select('div.fp-one-cita').__getitem__(0).text
    img = html.find_all('img').__getitem__(1).get('src')
    print(content + "  " + img)
    list.append(img)
    list.append(content)
    return list



def mail():
    list = spider();
    ret = True
    try:
        mail_msg ='<p>'+list[1]+'</p><p><img src="'+list[0]+'"></p>'
        msg = MIMEText(mail_msg, 'html', 'utf-8')
        msg['From'] = formataddr(['huzai', my_sender])
        # msg['To'] = ','.join(receiver)
        msg['Subject'] ="今日份语录"
        server = smtplib.SMTP_SSL('smtp.qq.com', 465)
        server.login(my_sender, my_pwd)
        server.sendmail(my_sender, receiver, msg.as_string())
        server.quit()
    except Exception:
        ret = False
    return ret


ret = mail()
if(ret):
    print('邮件发送成功')
else:
    print('邮件发送失败')

