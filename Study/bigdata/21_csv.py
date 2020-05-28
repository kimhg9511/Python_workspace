import csv
from collections import namedtuple as nt
data = []
headers = ['Symbol', 'Price', 'Date', 'Time', 'Change', 'Volume']
rows = [
    ("AA", 39.48, "6/11/2007", "9:36am", -0.18, 181800),
    ("AIG", 71.38, "6/11/2007", "9:36am", -0.15, 195500),
    ("AXP", 62.58, "6/11/2007", "9:36am", -0.46, 935000),
    ("BA", 98.31, "6/11/2007", "9:36am", +0.12, 104800),
    ("C", 53.08, "6/11/2007", "9:36am", -0.25, 360900),
    ("CAT", 78.29, "6/11/2007", "9:36am", -0.23, 225400)
]
dictRows = [{'Symbol':'AA', 'Price':39.48, 'Date':'6/11/2007',
          'Time':'9:36am', 'Change':-0.18, 'Volume':181800},
        {'Symbol':'AIG', 'Price': 71.38, 'Date':'6/11/2007',
          'Time':'9:36am', 'Change':-0.15, 'Volume': 195500},
        {'Symbol':'AXP', 'Price': 62.58, 'Date':'6/11/2007',
          'Time':'9:36am', 'Change':-0.46, 'Volume': 935000},
        ]
# with open('stock.csv') as stock:
#     stock_csv = csv.reader(stock)
#     headers = next(stock_csv)
#     data.append(headers)
#     content = []
#     for row in stock_csv:
#         data.append(row)

# for row in data:
#     print(row)
# ntData = nt('ntData', data[0])
# for row in data[1:]:
#     ntRow = ntData(*row)
#     print(f'ntRow: {ntRow.Symbol}, {ntRow.Change}')
# print(ntData)
#
# with open('stock.csv') as stock:
#     stock_csv = csv.DictReader(stock)
#     for row in stock_csv:
#         print(row)

with open('stocks_new01.csv', 'w') as stock_new01:
    stock_new01_csv = csv.writer(stock_new01)
    stock_new01_csv.writerow(headers)
    stock_new01_csv.writerows(rows)

with open('stocks_new02.csv', 'w') as stock_new02:
    stock_new02_csv = csv.DictWriter(stock_new02, headers)
    stock_new02_csv.writeheader()
    stock_new02_csv.writerows(dictRows)
