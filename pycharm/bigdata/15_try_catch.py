# try, except, else, finally, raise
class NotThreeMultipleError(Exception):
    def __init__(self):
        super().__init__('3의 배수')


def ten_div(x):
    try:
        x = int(input('나눌 숫자를 넣으세요'))
        assert x <= 10, '10보다 큰 값'
        if x % 3 == 0:
            raise NotThreeMultipleError
        y = 10 / x
    except Exception as e:
        y = e
    else:
        print('정상처리됨')
    finally:
        print('무조건 실행')
    return y


print(ten_div(0))
