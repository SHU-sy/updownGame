# updown game
# 반복문, 조건, 함수
# 5회 안에 맞혀야 성공 틀리면 실패
# TODO 코드 함수로 바꾸기
# TODO + 코인 시스템
# TODO + 칭호 시스템
# TODO + 상점 시스템
# TODO + 재도전 시스템
# TODO 일정 확률로 얻는 코인 2배

import random

com_num = random.randrange(1, 101)

for i in range(1, 6):
    peo_num = int(input("숫자를 입력해주세요 : "))

    if (peo_num == com_num):
        print("성공!!!")
        break

    elif (i == 5):
        print("실패!!!")
        break

    else:
        if (peo_num > com_num):
            print("down!")
        else:
            print("up!")

        print("{}번의 기회가 남았습니다 다시 입력해주세요.".format(5 - i))