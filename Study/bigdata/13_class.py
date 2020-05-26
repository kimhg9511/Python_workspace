# class Person:
#     def __init__(self):
#         print('__init__')
#         self.hello = '안녕하세요'
#     def greeting(self):
#         print(self.hello)
#
#     def helloeng(self):
#         print("i'm hello()..", end=" ")
#         self.greeting()
#
# james = Person();
# james.greeting()
# james.helloeng()
# print(isinstance(james, Person))
#
# def factorial(n):
#     if not isinstance(n, int) or n < 0 :
#         return None
#     if n == 1:
#         return 1
#     return n * factorial(n-1)
#
# print(factorial(7))
#
# class Student:
#     __slots__ = ['hello', 'name', 'age', '__address', 'email', '__wallet']
#
#     def __init__(self, **kwargs):
#         self.hello = '안녕하세요'
#         self.name = kwargs['name']
#         self.age = kwargs['age']
#         self.__address = kwargs['address']
#         self.__wallet = 1000000
#
#     def greeting(self):
#         print('{} 저는 {} 입니다.'.format(self.hello, self.name))
#
#     def __getWallet(self):
#         return self.__wallet
#
#     def pay(self, amount):
#         if amount > self.__wallet:
#             print('잔액 부족')
#         else:
#             self.__wallet -= amount
#             print('사용: {}, 남은돈: {}'.format(amount, self.__wallet))
# hong = Student(**{'name': '홍길동', 'age': 16, 'address': '율국'})
# hong.greeting()
# hong.email = 'email'
# print(f'{hong.name}, {hong.age}, {hong.email}')
#
# maria = Student(**{'name': '마리아', 'age': 16, 'address': '반포동'})
# maria.greeting()
# # print(dir(maria))  # doesn't have email
# print(f'{maria.name}, {maria.age}')
#
# for i in range(10):
#     hong.pay(100000)
class Knight:
    def __init__(self, health, mana, armor):
        self.health = health
        self.mana = mana
        self.armor = armor

    def slash(self):
        print('베기')

x = Knight(health=542.4, mana=210.3, armor=38)
print(x.health, x.mana, x.armor)
x.slash()
class Book:
    bag = []

    @staticmethod
    def put_bag(stuff):
        Book.bag.append(stuff)

    @classmethod
    def print_count(cls):
        print('{}'.format(cls.bag))
j = Book()
Book.put_bag('book')
m = Book()
Book.put_bag('book2')
print(m.bag)