import requests
from bs4 import BeautifulSoup
import json
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
req = requests.get('https://beomi.github.io/beomi.github.io_old/')

html = req.text
soup = BeautifulSoup(html, 'html.parser')

my_titles = soup.select(
    'h3 > a'
)
data = {}
for title in my_titles:
    data[title.text] = title.get('href')

with open(os.path.join(BASE_DIR, 'result.json'), 'w+', encoding='UTF-8-sig') as json_file:
    json_file.write(json.dumps(data, ensure_ascii=False))

with open(os.path.join(BASE_DIR, 'result.json'), 'r+', encoding='UTF-8-sig') as json_file:
    data = json.load(json_file)
    for k, v in data.items():
        print(v)