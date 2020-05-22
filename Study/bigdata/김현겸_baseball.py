# 야구게임 3자리
import random as r
isCorrect = False
randomNumber = ''
resultSet = []
while len(set(randomNumber)) != 3:
    randomNumber = '{0:0>3}'.format(r.randint(0, 999))
while not isCorrect:
    # print(randomNumber) # for test : computer number
    answer = input('3자리 숫자를 입력하세요(0~999 중복없이): ')
    # invalid input
    if len(set(answer)) != 3 or len(answer) != 3 or not answer.isnumeric():
        print('올바른 값을 입력하세요')
        continue
    # correct answer
    if randomNumber == answer:
        print(f'정답! {len(resultSet)+1}번만에 맞추셨군요')
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

