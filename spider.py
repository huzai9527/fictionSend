import requests
import re
from bs4 import BeautifulSoup
def spider():
    list = []
    response = requests.get('https://www.xbiquge6.com/13_13134/')
    response.encoding = ('utf-8')
    html = response.text
    html = BeautifulSoup(html, 'html.parser')
    time = html.select('div#info p:nth-of-type(3)').__getitem__(0).text[5:]
    title = html.select('div#info p:nth-of-type(4) a[href]').__getitem__(0).text
    href = html.select('div#info p:nth-of-type(4) a[href]').__getitem__(0)
    print(title)
    pattern = re.compile(r'href="(.+?)"')
    href = re.findall(pattern, href.__str__()).__getitem__(0)
    href = "https://www.xbiquge6.com"+href
    response = requests.get(href)
    response.encoding = ('utf-8')
    html = BeautifulSoup(response.text, 'html.parser')
    content = html.select('div#content')
    list.append(title)
    list.append(content)
    return list

