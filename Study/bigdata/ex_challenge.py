# # 구구단
# gugudan = [[i, j, i*j] for j in range(1, 10) for i in range(2, 10)]
# for dan in gugudan:
#     # print(dan[0], '*', dan[1], '=', dan[2], end='\t' + '\n' * (dan[0] % 9 == 0))
#     print(f'{dan[0]} * {dan[1]} = {dan[2]}', end='\t' + '\n' * (dan[0] % 9 == 0))
#
# # FizzBuzz 3의 배수: 'Fizz' 5의 배수: 'Buzz'
# multiples = {3: 'Fizz', 5: 'Buzz', 7: 'Sizz'}
# for i in range(1, 101):
#     sMultiples = ''
#     for key, val in multiples.items():
#         sMultiples += val * (i % key == 0)
#     print(sMultiples or i)
#
# # 문자열 중 길이가 5인 것들만 리스트 형태로 출력되게 만드시오
# nato = ['alpha', 'bravo', 'charlie', 'delta', 'echo', 'foxtrot', 'golf', 'hotel', 'india']
# print([one for one in nato if len(one) == 5])
#
# # 컴퓨터가 숫자 1개를 내면 맞추는 예제(0~99)
# import random as r
# com = r.randint(0, 99)
# isCorrect = False
# count = 0
# while not isCorrect:
#     count += 1
#     answer = input('맞춰보세요(0~99): ')
#     if answer.isnumeric():
#         answer = int(answer)
#     else:
#         print('잘못된 값입니다.')
#         continue
#     if answer == com:
#         print(f'정답! {count}번만에 맞추셨군요')
#         isCorrect = True
#     elif answer < com:
#         print(f'{answer}보단 커요')
#     else:
#         print(f'{answer}보단 작아요')
#
# 야구게임 3자리
import random as r
isCorrect = False
randomNumber = ''
resultSet = []
while len(set(randomNumber)) != 3:
    randomNumber = '{0:0>3}'.format(r.randint(0, 999))
while not isCorrect:
    print(randomNumber)
    answer = input('3자리 숫자를 입력하세요(0~999 중복없이): ')
    # invalid input
    if len(set(answer)) != 3 or len(answer) != 3 or not answer.isnumeric():
        print('올바른 값을 입력하세요')
        continue
    # correct answer
    if randomNumber == answer:
        print('정답!')
        isCorrect = True
    # incorrect answer & hint
    else:
        strike = [int(c) - int(u) for c, u in zip(randomNumber, answer)].count(0)
        out = sum([0 if randomNumber.count(i) else 1 for i in answer])
        ball = 3 - strike - out
        resultSet.append(f'[{answer}] : {strike}S {ball}B {out}O')
        print('오답! hint:')
        for result in resultSet:
            print(result)



