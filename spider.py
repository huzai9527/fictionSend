import requests
import re
from bs4 import BeautifulSoup
response = requests.get('http://wufazhuce.com/')
html = response.text
html = BeautifulSoup(html, 'html.parser')
content = html.select('div.fp-one-cita').__getitem__(0).text
img = html.find_all('img').__getitem__(1).get('src')
print(content+"  "+img)

