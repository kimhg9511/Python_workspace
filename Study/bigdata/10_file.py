# fileobj = open(filename, mode)
# # fileobj.write('content')
# file = open('hello.txt', 'w')  # mode : w, r, a ...
# print(type(file))  # <class '_io.TextIOWrapper'>
# file.write('hello, world!!')
# file.close()
#
# # fileobj.read()
# file = open('hello.txt', 'r')
# s = file.read()
# print(s)
# file.close()
#
# # with open
# with open('hello.txt', 'r') as file:
#     s = file.read()
#     print(s)
#
# # file + sequence
# lines = ['hello\n', 'python\n', 'coding dojang\n']
# lines2 = []
# with open('hello.txt', 'w') as file:
#     file.writelines(lines)
# with open('hello.txt', 'r') as file:
#     for line in file:
#         print(line, end='')
#     # a, b, c = file
#     # print(a, b, c, sep='')
#
# # pickle object <=> file unpickle
# import pickle as p
# name = 'james'
# age = 17
# address = '구로'
# scores = {'korean': 90, 'english': 95, 'math': 85, 'science': 82}
#
# with open('james.p', 'wb') as file:
#     p.dump(name, file)
#     p.dump(age, file)
#     p.dump(address, file)
#     p.dump(scores, file)
#
# with open('james.p', 'rb') as file:
#     name2 = p.load(file)
#     age2 = p.load(file)
#     address2 = p.load(file)
#     scores2 = p.load(file)
#     print(name2)
#     print(age2)
#     print(address2)
#     print(scores2)
#
# word.txt 읽어서 10자 이하인 단어의 개수와 단어명을 출력되게 만드시오.
with open('words.txt', 'r') as file:
    words = file.readlines()
    words = [word for word in words if len(word.strip(' \n')) <= 10]
    for word in words:
        print(word.strip('\n'))
    print('total:', len(words))


