# # tuple() () 읽기모드 ArrayList index 0
# a = (10, "Python", True, 4.4, '50')
# print(a)
# print(type(a))
#
# # initialize
# a = (40,)
# print(a)
#
# # init + range()
# a = tuple(range(10))
# print(a)
# a = tuple(range(10, 0, -1))
# print(a)
#
# # list <=> tuple
# a = [1, 2, 3]0
# b = tuple(a)
# c = list(b)
# print(b)
# print(c)
#
# # list('')
# print(list('Hello'))
# print(tuple('Hello'))
#
# # list, tuple 변수
# a, b, c = (1, 2, 3)
# d, e, f = [1, 2, 3]
# print(a, b, c)
# print(d, e, f)
# print(a+b, a+d)
# # unpacking
# x = [1, 2, 3]
# ax, bx, cx = x
# print(x)
# print(ax, bx, cx)
# y = (1, 2, 3)
# ay, by, cy = y
# print(y)
# print(ay, by, cy)
#
# # quiz [5, 3, 1, -1, -3, -5, -7, -9]
# print(list(range(5, -10, -2)))
#
# a = tuple(range(0,100,10))
# print(a)
# # index(value)
# print(a.index(30))  # 4
#
# # count(value)
# print(a.count(40))  # 1
#
# # tuple comprehension
# a = tuple(i for i in range(10) if i % 2 == 0)
# print(a)  # (0, 2, 4, 6, 8)
#
# # map
# a = (1.2, 2.5, 3.7, 4.6)
# a = tuple(map(int, a))
# print(a)  # (1, 2, 3, 4)
#
# min, max, sum
a = (38, 21, 53, 62, 19)
print(min(a))  # 19
print(max(a))  # 62
print(sum(a))  # 193
