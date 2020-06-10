```python
from bs4 import BeautifulSoup as bs
import requests
import re
```


```python
# load html
url = 'https://www.wikitree.co.kr/articles/217101'
resp = requests.get(url)

# dataset
soup = bs(resp.text.replace('&nbsp;', ' '),'html.parser')
news_content = soup.select_one('div#wikicon')
store_list = []
tel_list = []
addr_list = []
stores = list(map(lambda i : i.text.split('회 '), news_content.select('strong')))
tel_p = re.compile('^\d{2,3}-\d{3,4}-\d{4}')
addr_p = re.compile('^[가-힣 ]{0,4}시?[가-힣]{1,3}구 [가-힣]{0,3}동?')

# create each list
for store in stores:
    if len(store) > 1:
        store_list.append(store[-1])
tel_list = news_content.find_all(string = tel_p)
addr_list = news_content.find_all(string = addr_p)
store_total = [(store.strip(), tel.strip(), addr.strip()) for store,tel,addr in zip(store_list, tel_list, addr_list)]

# test 
for item in store_total:
    print(item)
```

    ('다성일식', '02-338-8951', '서울시 서대문구 창천동 72-36')
    ('봉산집', '02-793-5022', '서울시 용산구 용산동3가 1-21')
    ('창고43', '02-786-5959', '한우모둠구이, 깍두기볶음밥, 된장찌개')
    ('돕감자탕', '02-499-2838', '서울시 영등포구 여의도동 44-37 아일렉스타워15층(스카이점)')
    ('대보명가', '02-907-6998', '서울시 광진구 화양동 9-22')
    ('해뜨는집', '02-764-6354', '서울시 강북구 수유동 563-14')
    ('아이 해브어 드림', '02-3453-7696', '서울시 성북구 동소문동 1가 62')
    ('아현동 간장게장', '02-312-7530', '서울시 강남구 역삼동 821 이즈타워 B3')
    ('왕소금구이', '02-545-6844', '서울시 마포구 아현동  282-1')
    ('라틀리에 모니크', '02-549-9210', '서울시 강남구 논현동 98-12')
    ('비스트로 딩고', '02-518-7866', '서울시 강남구 청담동 80-21')
    ('줄리에뜨', '02-535-4002', '서울시 강남구 신사동 526-11')
    ('충주집', '02-923-1068', '서울시 서초구 반포4동 82-22')
    ('영화루', '02-738-1218', '서울시 동대문구 제기동 138-2')
    ('일품헌', '02-574-7117', '서울시 종로구 누하동 25-1')
    ('립스테이크', '02-379-2581', '서울시 서초구 양재동 1-28')
    ('오가와', '02-735-1001', '서울시 종로구 부암동 208-37')
    ('까사디노아', '02-3142-1108', '종로구 당주동 5 로얄빌딩 지하 1층')
    ('충무로 주꾸미 불고기', '02-2279-0803', '서울 마포구 연남동 257-8')
    ('애성회관', '02-352-0303', '서울 중구 필동 1가 3-20')
    


```python
()
```
