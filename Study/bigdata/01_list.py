# # list() [] 배열, ArrayList index 0
# a = [10, "Python", True, 4.4, '50']
# print(a)
# print(type(a))
#
# # initialize
# a = []
# b = list()
#
# # init + range()
# r = list(range(10))
# print(r)
# r = list(range(5, 12))
# print(r)
# r = list(range(-4, 10, 2))
# print(r)
# r = list(range(10, 0, -1))
# print(r)
#
# a = [0, 1, 2, 3, 4]  # **********
# # append
# a.append([10, 20])
# a.append({'name': 'kimhg'})
# print(a)  # [0, 1, 2, 3, 4, [10, 20], {'name': 'kimhg'}]
#
# # extend
# a.extend([40,50]) # a[len(a):] = [40,50]
# print(a)  # [0, 1, 2, 3, 4, 40, 50]
#
# # insert
# a.insert(2, 100)
# print(a)  # [0, 1, 100, 2, 3, 4]
#
# # extend at index (slice)
# a[2:2] = [100, 200]
# print(a)  # [0, 1, 100, 200, 2, 3, 4]
#
# # pop(index)
# for i in range(len(a)):
#     print(a.pop(), end=' ')  # 4 3 2 1 0
# print()
# print(a)  # []
#
# # del
# del a[1]
# print(a)  # [0, 2, 3, 4]
# #
# # remove(value)
# a = list(map(lambda i: i*10, a))  # **********
# a.remove(20)
# print(a)  # [0, 10, 30, 40]
#
# # index(value)
# print(a)
# print(a.index(10))  # 1
#
# # count(value)
# a.append(20)
# print(a)  # [0, 10, 20, 30, 40, 20]
# print(a.count(20))  # 2
#
# # reverse
# a.reverse()
# print(a)  # [40, 30, 20, 10, 0]
#
# # sort
# a.extend([15, 25, 35])
# print(a)  # [0, 10, 20, 30, 40, 15, 25, 35]
# a.sort()  # ascending
# print(a)  # [0, 10, 15, 20, 25, 30, 35, 40]
# a.sort(reverse=True)  # descending
# print(a)  # [40, 35, 30, 25, 20, 15, 10, 0]
#
# # sorted(copy)
# b = sorted(a)  # a[:] & b.sort()
# print(b)  # [0, 10, 20, 30, 40]
#
# # clear
# a.clear()  # del a[:]
# print(a)  # []
#
# # isEmpty
# if not len(a):
#     pass
# if not a:
#     pass
#
# # copy
# b = a.copy()
# print(a is b)  # False
# print(a == b)  # True
#
# # enumerate
# for i, v in enumerate(a, start=1):
#     print(i, v, end=",")  # 1 0,2 10,3 20,4 30,5 40,
#
# # min, max
# print(a)  # [0, 10, 20, 30, 40]
# print(max(a))  # 40
# print(min(a))  # 0
#
# # sum
# print(a)  # [0, 10, 20, 30, 40]
# print(sum(a))  # 100
#
# # list comprehension
# a = [i for i in range(10) if i % 2 == 0]
# print(a)  # [0, 2, 4, 6, 8]
#
# map
a = [1.2, 2.5, 3.7, 4.6]
a = list(map(int, a))
print(a)  # [1, 2, 3, 4]
inputSum = sum(list(map(int, input().split())))
print(inputSum)