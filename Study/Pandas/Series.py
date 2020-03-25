from pandas import Series, DataFrame

# 0:Series는 인덱스값을 직접 지정할 수 있다.(Key-Value의 리스트)
kakao = Series([92600, 92400, 92100, 94300, 92300],
index=['2016-02-19', '2016-02-18', '2016-02-17', '2016-02-16', '2016-02-15'])
# 1:전체 출력(인덱스 - 값)
print("----------output 1----------")
print(kakao)
# 2:지정한 인덱스로 해당하는 값 호출
print("----------output 2----------")
print(kakao['2016-02-19'])
print(kakao['2016-02-18'])
# 3:.index로 인덱스에 대응되는 1차원 배열을 불러온다
print("----------output 3----------")
for date in kakao.index:
    print(date)
# 4:.values로 값에 대응되는 1차원 배열을 불러온다
print("----------output 4----------")
for ending_price in kakao.values:
    print(ending_price)
# 5.Series의 덧셈은 인덱스 순서가 달라도 같은 인덱스끼리 덧셈을 수행한다.
print("----------output 5----------")
mine = Series([10, 20, 30], index=['naver', 'sk', 'kt'])
friend = Series([10, 30, 20], index=['kt', 'naver', 'sk'])
merge = mine + friend
print(merge)



