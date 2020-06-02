# # replace
# s = 'Hello, world'.replace('world', 'Python')
# print(s)  # Hello, Python
#
# # split, join
# fruit = 'apple pear grape pineapple orange'
# fruit = fruit.split()
# print(fruit)  # ['apple', 'pear', 'grape', 'pineapple', 'orange']
# fruit = ' '.join(fruit)
# print(fruit)  # apple pear grape pineapple orange
#
# # etc utils(upper, lower, lstrip, rstrip, strip)
# print('python'.upper())  # PYTHON
# print('PYTHON'.lower())  # python
# print('      python          '.lstrip())  # python       *
# print('      python          '.rstrip())  # *      python
# print('      python          '.strip())  # *python*
# print(',      python          '.lstrip(','))  # *      python          *
# print(', ,  .   python  ,  . ,  .   '.strip(' ,.'))  # *python*
#
# # find index count
# print('apple pineapple'.find('pl'))  # 2 (index)
# print('apple pineapple'.find('xy'))  # -1
# print('apple pineapple'.index('pl'))  # 2 (index)
# # print('apple pineapple'.index('xy'))  # error
# print('apple pineapple'.count('pl'))  # 2
#
#
# # formatting
# fruit = 'apple'
# s = 'Today is %s %s.' % (fruit, 'April')
# print(s)  # Today is apple April.
# hello = 'Hello, {0}, {2}, {1}'
# print(hello.format('world0', 'world1', 'world2'))  # Hello, world0, world2, world1
# print('{0: ^10s}'.format('python'))
#
# 전체 경로에서 file 이름 가져오기
path = 'C:\\Users\\dojang\\AppData\\Local\\Programs\\Python\\Python36-32\\python.exe'
div = '\\'
# path = path.split(div)[-1]
path = path[path.rfind('\\') + 1:]
print(path)
