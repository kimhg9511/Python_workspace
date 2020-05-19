# x = 10
# if x == 10:
#     print("10입니다.")
# elif x == 20:
#     print("20입니다.")
# else:
#     print("???")
#
# # A 기업의 입사 시험은 필기 시험 점수가 80점 이상 && 코딩 시험을 통과(True/False)해야 합격 / 불합격
# written_test = 75
# coding_test = True
# if written_test >= 80 and coding_test:
#     print("합격")
# else:
#     print("불합격")
#
# # 사용자 값을 하나 받고 1번이면 콜라, 2번이면 사이다, 3번이면 환타
# button = input('번호를 누르세요')
# if button == '1':
#     print("콜라")
# elif button == '2':
#     print("사이다")
# elif button == '3':
#     print("환타")
# else:
#     print("?")
#
# # 11~20 '11~20', 21~30 '21~30', ? '아무것도 해당되지 않음'
# x = int(input('번호 입력'))
# if 11 <= x <= 20:
#     print('11~20')
# elif 21 <= x <= 30:
#     print('21~30')
# else:
#     print('아무것도 해당되지 않음')
#
# # 홀짝 판별
# num = int(input('숫자 입력'))
# if num % 2 == 0:
#     print('짝수')
# else:
#     print('홀수')
#
# # 사용자 값 + 20, 단 최대:255
# num = int(input('숫자 입력'))
# if num >= 236:
#     print(255)
# else:
#     print(num+20)
#
# # 사용자로부터 입력 받은 시간이 정각인지 판별
# # input) 02:00 '정각'
# # input) 02:22 '정각 아님'
# time = input('시각을 입력하세요 00:00 >> ')
# minute = time.split(':')[-1]
# if minute == '00':
#     print('정각')
# else:
#     print('정각 아님')
#
# # 좋아하는 과일은?
# fruit = ['사과', '포도', '홍시']
# favorite = input("좋아하는 과일은? ")
# if favorite in fruit:
#     print('정답')
# else:
#     print('오답')
# # 문자열 1개를 입력받아 소문자 => 대문자, 대문자 => 소문자
# s = input('알파벳 1개 입력: ')
# if s.islower():
#     print(s.upper())
# elif s.isupper():
#     print(s.lower())
# else:
#     print("????")
#
# # 주민등록번호 남녀판별(1,3=남자, 2,4=여자)
# # 지역판별(00~08=서울, 09~12=부산)
# code = '951117-1114567'
# gender = int(code[7])
# sCity = code[8:10]
# if code[9] == '0':
#     city = int(code[10])
# else:
#     city = int(code[8:10])
# if gender == 1 or gender == 3:
#     print("남자")
# elif gender == 2 or gender == 4:
#     print("여자")
# else:
#     print("?????")
# if 0 <= city <= 8:
#     print("서울 출생")
# elif 9 <= city <= 12:
#     print("부산 출생")
# else:
#     print("?????")
