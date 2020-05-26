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
# # closure
# def calc():
#     a = 3
#     b = 5
#     total = 0
#     def mul_add(x):
#         nonlocal total
#         total = total + a * x + b
#         print(total)
#     return mul_add
# c = calc()
# c(1)
# c(2)
# c(3)
#
# 호출 횟수를 세는 함수
def counter():
    i = 0

    def count():
        nonlocal i
        i += 1
        return i
    return count

class Counter:
    j = 0

    def count(self):
        self.j += 1
        return self.j

c = counter()
classC = Counter()
for i in range(10):
    print(c(), end=' ')
    print(classC.count(), end=' ')
print()
print(classC.j)
# print(c.i)  # error!
print(dir(c.__closure__[0]))
