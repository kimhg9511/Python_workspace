# 사전작업 : terminal 에서 pip install requests
# pip search
# pip list
# pip uninstall
import requests
response = requests.get('http://www.google.co.kr')
print(dir(response))
# print(response.text)

import module_square
print(module_square.base)
print(module_square.square(10))

import module_person
maria = module_person.Person('maria', 20, '명동')
maria.greeting()

import module_name
print("main.py's __name__", __name__)

import module_calc as calc
print(calc.add(1, 2))
print(calc.mul(3, 5))

from package_calc.operation import add, mul
from package_calc.geometry import triangle_area as ta, rectangle_area as ra
print(add(100, 200))
print(mul(100, 200))
print(ta(30, 40))
print(ra(30, 40))

