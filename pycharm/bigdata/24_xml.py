import requests as req
from urllib.request import urlopen
from xml.etree.ElementTree import parse
url = 'http://planet.python.org/rss20.xml'
response = urlopen(url)
data = parse(response)
print(data)
cnt = 0
items = []
for item in data.iterfind('channel/item'):
    title = item.findtext('title')
    date = item.findtext('pubDate')
    link = item.findtext('link')
    items.append({'title': title, 'date': date, 'link': link})
print(items)