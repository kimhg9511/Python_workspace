import requests
from bs4 import BeautifulSoup

naver_url = "https://www.naver.com/"

html = requests.get(naver_url).text
soup = BeautifulSoup(html, 'html.parser')
elem_list = soup.select('#rtk.group_keyword')

# print(soup)
print(elem_list)
