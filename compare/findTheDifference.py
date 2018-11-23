import re
import requests
from bs4 import BeautifulSoup
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




# content = spider().__getitem__(1).__str__().encode('utf-8')
# print(content.decode('utf-8'))
# with open('1.txt', 'wb+') as f:
#     f.write(content)

origin = open('1.txt', 'rb').read()
now = open('2.txt', 'r').read()
for i in range(0, len(now)):
    if origin[i] != now[i]:
        print(now[i:])
        break
