from pandas import Series, DataFrame

# 1:DataFrame 객체 생성: Dictionary를 사용하여 값 전달
print("----------output 1----------")
raw_data = {
    'col0': [1, 2, 3, 4],
    'col1': [10, 20, 30, 40],
    'col2': [100, 200, 300, 400]
}
data = DataFrame(raw_data)
print(data)
# 2:column 이름을 이용하여 '열'에 해당하는 데이터 접근 가능
print("----------output 2----------")
print(data['col0'])
print(data['col1'])
print(data['col2'])
# 3:type 함수를 사용하여 DataFrame에 있는 칼럼의 타입을 확인 : Series
print("----------output 3----------")
print(type(data['col0']))
# 4:DataFrame의 인덱스를 개발자가 지정한 값으로 할 수 있다.
print("----------output 4----------")
daeshin = {'open':  [11650, 11100, 11200, 11100, 11000],
           'high':  [12100, 11800, 11200, 11100, 11150],
           'low' :  [11600, 11050, 10900, 10950, 10900],
           'close': [11900, 11600, 11000, 11100, 11050]}
daeshin_day = DataFrame(daeshin)
date = ['16.02.29', '16.02.26', '16.02.25', '16.02.24', '16.02.23']
daeshin_day = DataFrame(daeshin, columns=['open', 'high', 'low', 'close'], index=date)
print(daeshin_day)
# 5:row값을 접근하기 위한 방법
print("----------output 5----------")
# print(daeshin_day['16.02.24']) 에러! dashin_day를 키 값(열의 값)으로 판단하게 됨.
# 보고자 하는 것은 행의 값
day_data = daeshin_day.loc['16.02.24']
print(day_data)
# row값도 Series 형태로 저장됨을 확인
print(type(day_data))