# # 변수의 범위
# x = 10  # 전역 변수(global variable)
# def foo():
#     x = 20  # 지역 변수(local variable)
#     print(x)  # 20
# foo()
# print(x)  # 10
#
# def foo():
#     x = 20
#     y = 30
#     return locals()
# dictTest = foo()
# print(dictTest['x'])
#
# closure
def calc():
    a = 3
    b = 5
    total = 0
    return lambda x: a * x + b
c = calc()
print(c(1), c(2), c(3), c(4), c(5))
