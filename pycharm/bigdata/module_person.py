class Person:
    def __init__(self, name, age, addr):
        self.name = name
        self.age = age
        self.addr = addr

    def greeting(self):
        print(f'hello my name is {self.name}')
