# import
import re
# # re.match('target', 'origin') - return : re.Match obj
# # re.search('target', 'origin') - return : re.Match obj
# # re.findall('target', 'origin') - return : list
# # ^ : start with, $ : end with, | : or
# print(re.match('^hello', 'hello world'))
# print(re.match('world$', 'hello world! hello'))
# print(re.findall('hello|world', 'hello world! hello'))
# # [-] : range
# print(re.findall('[0-9]', '1234'))
# # * : 0개 이상, + : 1개 이상
# print(re.match('a*b', 'b'))  # <re.Match object; span=(0, 1), match='b'>
# print(re.match('a+b', 'b'))  # None
# # ? : 0 or 1, . : 1
# print(re.findall('a?b', 'caacb ddd ab'))  # ['b', 'ab']
# # {n} : n개, {n,m} : n개부터 m개까지
# print(re.findall('h{3}', 'hello hhello hhhello hhhhhhello'))  # ['hhh', 'hhh', 'hhh']
# print(re.match('[0-9]{2,3}-[0-9]{3,4}-[0-9]{4}', '010-123-2345'))
# print(re.findall('[a-zA-z0-9.]+', 'hello1234@email.com'))  # ['hello1234', 'email.com']
# # [^-] : not
# print(re.findall('[^A-Z]+', 'hello Hello 1234H'))  # ['hello ', 'ello 1234']
# # 특수문자 찾기, \d \D \w \W \s \S
# print(re.findall('\*\*', '1 ** 2'))
# print(re.findall('[$()\w\d]+', '$(document)'))
# print(re.findall('[a-zA-Z0-9\t]+', 'asd  asd\tasd\nasd'))
# # compile
# rex = re.compile('([0-9]+) ([0-9]+)')
# data = '10 295'
# result = rex.match(data)
# print(result.group())  # 10 295
# print(result.group(1))  # 10
# print(result.group(2))  # 295
# print(result.groups())  # ('10', '295')
#
# email
p = re.compile('^[a-zA-Z0-9\-+._]+@[a-zA-Z0-9\-]+\.[a-zA-Z0-9.]+$')
emails = ['python@mail.example.com', 'python+kr@example.com',
          'python-dojang@example.co.kr', 'python_10@example.info',
          'python.dojang@e-xample.com',
          '@example.com', 'python@example', 'python@example-com',
          'python@example123.a123']
for email in emails:
    print(f'{email} : {p.match(email) is not None}')