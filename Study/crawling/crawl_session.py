import requests
from bs4 import BeautifulSoup as bs
# s = requests.Session()
# req = s.get('https://mail.google.com/mail/u/0/?tab=wm#inbox')
# html = req.text
# print(html)
LOGIN_INTO = {
    'userId': 'kimhgedu',
    'userPassword': 'test'
}
with requests.Session() as s:
    first_page = s.get('https://mail.google.com/')
    html = first_page.text
    status = first_page.status_code
    is_ok = first_page.ok
    print(f'status: {status}, ok: {is_ok}')
    soup = bs(html, 'html.parser')
    # csrf = soup.find('input', {'name': '_csrf'})
