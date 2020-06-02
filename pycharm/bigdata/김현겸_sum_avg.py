while True:
    numbers = input('5개의 숫자를 띄어쓰기로 입력해 주세요.').split()
    numbers = [int(number) if number.isnumeric() else 0 for number in numbers]
    if numbers.count(0) > 0 or len(numbers) != 5:
        print('다시 입력해 주세요.')
        continue
    break
numbersSum = sum(numbers)
print('합계 :', numbersSum)
print('평균 :', int(numbersSum / len(numbers)))
