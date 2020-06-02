import pandas_datareader.data as web
import datetime
import matplotlib.pyplot as plt

start = datetime.datetime(2016, 2, 19)
end = datetime.datetime(2016, 3, 4)
# 1:start날짜부터 end날짜까지의 데이터를 수집
gs = web.DataReader("078930.KS", "yahoo", start, end)
print(gs)
# 2:2010/1/1일부터 데이터를 조회한 날 까지의 데이터를 수집
gs = web.DataReader("078930.KS", "yahoo")
gs.info()
# 3:차트 그래프 그리기
plt.plot(gs['Adj Close'])
plt.show()
# 4:차트 그래프 그리기(2)
plt.plot(gs.index, gs['Adj Close'])
plt.show()

