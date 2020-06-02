# # 1. hard coding
# def hello():
#     print('hello 함수 시작')
#     print('hello')
#     print('hello 함수 끝')
#
#
# def world():
#     print('world 함수 시작')
#     print('world')
#     print('world 함수 끝')
#
#
# hello()
# world()


# # 2. closure
# def trace(func):
#     def wrapper():
#         print(func.__name__, '함수 시작')
#         func()
#         print(func.__name__, '함수 끝')
#     return wrapper
#
#
# def hello():
#     print('hello')
#
#
# def world():
#     print('world')
#
#
# trace(hello)()
# trace(world)()


# 3. decorator
def trace(func):
    def wrapper():
        print(func.__name__, '함수 시작')
        func()
        print(func.__name__, '함수 끝')
    return wrapper


@trace
def hello():
    print('hello')


@trace
def world():
    print('world')


hello()
world()
