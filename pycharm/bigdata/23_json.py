import json
import requests as req

# json.dumps() : dict ==> str
data = {
    'name': 'ACME',
    'shares': 100,
    'price': 542.23
}
json_data = json.dumps(data)
print('content:', json_data)
print('type:', type(json_data))

# json.loads() : str ==> dict
response = req.get('http://thecoding.kr/test.json')
req_json_data = response.text
# {
#     "employees": [
#         {"firstName:": "Joo"}, {"lastName": "Duu"},
#         {"firstName:": "Koo"}, {"lastName": "Kuu"},
#         {"firstName:": "Loo"}, {"lastName": "Luu"}
#     ]
# }
req_data = json.loads(req_json_data)
print('content:', req_data)
print('type:', type(req_data))
for headers, lists in req_data.items():
    print(f'** {headers} **')
    for item in lists:
        print(f"index [{lists.index(item)}]")
        for k2, v2 in item.items():
            print("\t", k2, "\t:", v2)


