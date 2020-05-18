# # list tuple range str - 연속적 (sequence)>> 자리의 개념
# # 첫번째 자리에 첫번째 값이 있다 ... 마지막 자리에 마지막 값이 있다
#
# # 특정 값이 있는지 확인
# a = (10, 20, 30, 40, 50)
# print(30 in a)  # true
# print(60 in a)  # false
# print(60 not in a)  # true
#
# # +
# a = [0, 10, 20, 30]
# b = [9, 8, 7, 6]
# print(a + b)
#
# # ** range cannot use +
# # print(range(0, 10) + range(10, 20))  # error
# # suggestion
# print(list(range(0, 10)) + list(range(10, 20)))
#
# # string + int
# # print('Hello' + 10)  # error
# # suggestion
# print('Hello' + str(10))
#
# # *
# print([0, 10, 20, 30] * 3)
# print('* ' * 10)
#
# # len()
# print(len([0, 10, 20, 30])) # 4
# s = 'hello world'
# print(len(s))  # 11
# print(len(range(0, 10)))  # 10
# print(len('한글의 길이는'))  # 7
# print(len('한글의 길이는'.encode('utf-8')))  # 19
#
# index
a = (10, 20, 30, 40, 50)
print(a[0])  # 10
print(a.__getitem__(1))  # internal call, 20
# 음수 index
print(a[-1])  # 50
# 할당
a = list(a)
a[1] = 100
print(a)  # [10, 100, 30, 40, 50]
# del
del a[1]
print(a)  # [10, 30, 40, 50]



