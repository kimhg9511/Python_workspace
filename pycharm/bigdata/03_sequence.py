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
# # index
# a = (10, 20, 30, 40, 50)
# print(a[0])  # 10
# print(a.__getitem__(1))  # internal call, 20
# # 음수 index
# print(a[-1])  # 50
# # 할당
# a = list(a)
# a[1] = 100
# print(a)  # [10, 100, 30, 40, 50]
# # del
# del a[1]
# print(a)  # [10, 30, 40, 50]
#
# # slice
a = list(range(0, 100, 10))
# print(a)  # [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
# print(a[0:4])  # [0, 10, 20, 30], a[0] ~ a[3]
# print(a[4:-1])  # [40, 50, 60, 70, 80], a[4] ~ a[-2]
# print(a[2:8:3])  # [20, 50], a[2] ~ a[7] step: 3 => a[2], a[5]
# print(a[5:1:-1])  # [50, 40, 30, 20], a[5] ~ a[2] step: -1
# print(a[::-1])  # [90, 80, 70, 60, 50, 40, 30, 20, 10, 0], reverse
# print(a[:7])  # [0, 10, 20, 30, 40, 50, 60], (a[0]) ~ a[6]
# print(a[7:])  # [70, 80, 90], a[7] ~ (a[9])
#
# # slice + len
# print(a[:len(a)])  # [0, 10, 20, 30, 40, 50, 60, 70, 80, 90], equals a[:]
#
# # slice 대입
# b = a[:]  # 값 전달 (해당 데이터가 변경될 때 원본 데이터가 변경되지 않음)
# c = a  # 주소 전달 (해당 데이터가 변경될 때 원본 데이터가 변경됨)
# a[2:5] = ['a', 'b', 'c']
# print(a)  # [0, 10, 'a', 'b', 'c', 50, 60, 70, 80, 90], update a[2:5]
# a[2:5] = ['a']
# print(a)  # [0, 10, 'a', 50, 60, 70, 80, 90] update a[2], delete a[3],a[4]
# a[3:3] = ['a']
# print(a)
# a[:8:2] = ['a', 'b', 'c', 'd']  # ['a', 10, 'b', 30, 'c', 50, 'd', 70, 80, 90]
# print(a)
# 
# # slice 삭제
# del a[2:5]
# print(a)  # [0, 10, 50, 60, 70, 80, 90]
# del a[::2]
# print(a)  # [10, 30, 50, 70, 90]
# # quiz = 최근 3년간의 인구수 출력
# year = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]
# population = [10249679, 10195318, 10143645, 10103233, 10022181, 9930616, 9857426, 9838892]
# print(year[-3:])
# print(population[-3:])
# # quiz = 홀수인덱스 출력
# n = (-32, 75, 97, -10, 9, 32, 4, -15, 0, 76, 14, 2)
# print(n[1::2])
