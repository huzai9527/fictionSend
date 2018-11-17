import smtplib
from email.mime.text import MIMEText
import re
from bs4 import BeautifulSoup
import requests
from email.utils import formataddr
my_sender = "369212851@qq.com"
my_pwd = "tkkterceepmhbigi"
receiver = "369212851@qq.com"


def spider():
    list = []
    response = requests.get('https://www.xbiquge6.com/13_13134/')
    response.encoding = ('utf-8')
    html = response.text
    html = BeautifulSoup(html, 'html.parser')
    time = html.select('div#info p:nth-of-type(3)').__getitem__(0).text[5:]
    title = html.select('div#info p:nth-of-type(4) a[href]').__getitem__(0).text
    href = html.select('div#info p:nth-of-type(4) a[href]').__getitem__(0)
    # print(title)
    pattern = re.compile(r'href="(.+?)"')
    href = re.findall(pattern, href.__str__()).__getitem__(0)
    href = "https://www.xbiquge6.com" + href
    response = requests.get(href)
    response.encoding = ('utf-8')
    html = BeautifulSoup(response.text, 'html.parser')
    content = html.select('div#content')
    # print(content)
    list.append(title)
    list.append(content)
    list.append(time)
    return list


def mail():
    list = spider();
    ret = True
    try:
        mail_msg = list.__getitem__(1).__str__()
        msg = MIMEText(mail_msg, 'html', 'utf-8')
        msg['From'] = formataddr(['huzai', my_sender])
        msg['To'] = formataddr(['huzai', receiver])
        msg['Subject'] = list.__getitem__(0)
        server = smtplib.SMTP_SSL('smtp.qq.com', 465)
        server.login(my_sender, my_pwd)
        server.sendmail(my_sender, [receiver], msg.as_string())
        server.quit()
    except Exception:
        ret = False
    return ret


ret = mail()
if(ret):
    print('邮件发送成功')
else:
    print('邮件发送失败')

