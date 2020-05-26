# 함수 function()
# 클래스 = 메소드()
# 재사용 파라미터 리턴값
# # hello
# def hello():
#     print('hello, function')
# hello()
#
# # docstring
# def add(a, b):
#     """
#     a와 b를 더하여 반환하는 함수
#     :param a: 계산하는 값 1
#     :param b: 계산하는 값 2
#     :return: 계산 결과
#     """
#     return a+b
# c = add(1,2)
# print(c)
# print(add.__doc__)
# print(help(add))
#
# # return
# def not_ten(a):
#     if a == 10:
#         return
#     print(a, '입니다', sep='')
# not_ten(5)  # 5입니다
# not_ten(10)  # (blank)
#
# # return 2, more
# def calc(a, b):
#     add = a + b
#     sub = a - b
#     mul = a * b
#     if b == 0:
#         div = "can't calculate"
#         mod = "can't calculate"
#     else:
#         div = a / b
#         mod = a % b
#     return add, sub, mul, div, mod
# n1 = calc(3, 5)
# n2, n3, n4, n5, n6 = calc(3, 5)
# print(n1)  # (8, -2, 15, 0.6, 3), tuple
# print(n2, n3, n4, n5, n6)  # 8 -2 8 -2 15 0.6 3
#
# # 몫과 나머지
# def get_quotient_remainder(x, y):
#     return int(x / y), x % y
#
# x, y = 105, 9
# quotient, remainder = get_quotient_remainder(x, y)
# print(f'몫:{quotient}, 나머지:{remainder}')
#
# # 가변인자
# def personal_info(**kwargs):
#     for kw, arg in kwargs.items():
#         print(kw, ':', arg, sep='')
# x = {'name': '홍길동', 'age': 16, 'address': '율국'}
# print(*x)
# personal_info(*x)
#
# # max, min, avg
# korea, english, math, science = 100, 86, 81, 91
# def get_max_score(*args):
#     return max(args), min(args), sum(args) / len(args)
#
# max_score, min_score, avg_score = get_max_score(korea, english, math, science)
# print(f'MAX: {max_score}\nMIN: {min_score}\nAVG: {avg_score}\n')
# max_score, min_score, avg_score = get_max_score(math, english)
# print(f'MAX: {max_score}\nMIN: {min_score}\nAVG: {avg_score}\n')
#
# # 재귀함수
# def hello(count):
#     if count == 0:
#         return
#     count -= 1
#     print('Hello, world!')
#     hello(count)
# hello(10)
#
# # factorial & fivonachi
# def factorial(n):
#     if n == 1:
#         return 1
#     f = n * factorial(n-1)
#     return f
# print(factorial(5))
#
# # lambda expression - 함수를 짧게
# # def plus_ten(x):
# #     return x + 10
# # print(plus_ten(10))
# print((lambda x: x+10)(1))
# print(list(map(lambda x: x + 10, [1, 2, 3])))
#
# # lambda + map
# a = [i for i in range(1, 11)]
# data = list(map(lambda x: str(x) if x % 3 == 0 else x, a))
# print(data)
# a = [i for i in range(1, 6)]
# b = [i*2 for i in range(1, 6)]
# data = list(map(lambda x, y: x*y, a, b))
# print(data)
#
# # lambda + filter
# a = [8, 3, 2, 10, 15, 7, 1, 9, 0, 11]
# print(list(filter(lambda x: 5 < x < 10, a)))
#
# # lambda + reduce
# from functools import reduce
# a = [i for i in range(1, 6)]
# print(reduce(lambda x, y: x * y, a))
# print('my name is string'.find('string'))
#
# 이미지 파일만 가져오기(png, jpg) - lambda 사용
files = ['font', '1.png', '10.jpg', '11.gif', '2.jpg', '3.png', 'table.xslx', 'spec.docx']
print(list(filter(lambda x: x.endswith('.png') or x.endswith('.jpg'), files)))
