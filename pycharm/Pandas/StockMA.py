import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt

# 1:2014-01-01~2016-03-06의 야후 주가
gs = web.DataReader("078930.KS", "yahoo", "2014-01-01", "2016-03-06")
gs = web.DataReader("078930.KS", "yahoo")
# test : print(gs.tail())
# 2:5일 이동평균 ma5 생성
# Series.rolling() = 일정 범위만큼 반복계산
# rolling.mean() = 평균 계산
ma5 = gs['Adj Close'].rolling(window=5).mean()
ma20 = gs['Adj Close'].rolling(window=20).mean()
ma60 = gs['Adj Close'].rolling(window=60).mean()
ma120 = gs['Adj Close'].rolling(window=120).mean()
# test : print(ma5.tail(10))
# ma5를 DataFrame에 저장
gs.insert(len(gs.columns), "MA5", ma5)
gs.insert(len(gs.columns), "MA20", ma20)
gs.insert(len(gs.columns), "MA60", ma60)
gs.insert(len(gs.columns), "MA120", ma120)
# test : print(gs.tail())
# 종가,이동평균선 그래프 그리기
plt.plot(gs.index, gs['Adj Close'], label="Adj Close")
plt.plot(gs.index, gs['MA5'], label="MA5")
plt.plot(gs.index, gs['MA20'], label="MA20")
plt.plot(gs.index, gs['MA60'], label="MA60")
plt.plot(gs.index, gs['MA120'], label="MA120")
plt.legend(loc='best')
plt.grid()

plt.show()