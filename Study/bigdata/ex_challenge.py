# # 구구단
# gugudan = [[i, j, i*j] for j in range(1, 10) for i in range(2, 10)]
# for dan in gugudan:
#     print(dan[0], '*', dan[1], '=', dan[2], end='\t' + '\n' * (dan[0] % 9 == 0))
# FizzBuzz 3의 배수: 'Fizz' 5의 배수: 'Buzz'
multiples = {3: 'Fizz', 5: 'Buzz', 7: 'Sizz'}
for i in range(1, 101):
    sMultiples = ''
    for key, val in multiples.items():
        sMultiples += val * (i % key == 0)
    print(sMultiples or i)
