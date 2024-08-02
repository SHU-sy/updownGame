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

# 맞히는 숫자 설정
com_num = random.randrange(1, 101)

# life 개수 설정
life = 5

# level 설정
level = 1

# 현재 위치
def total(life, level):
    print("life : {}", life)
    print("level : {}", level)

# 입력한 숫자 검증
def number_check(peo_num, com_num, life, level):
    if peo_num == com_num:  # 추측한 숫자가 맞았을 경우
        print("성공!!!")
        level = level + 1
        return retry()

    elif life == 0:  # life 를 다 잃었을 경우
        print("실패!!!")
        return retry()

    else:  # 추측한 숫자가 틀렸을 경우
        if peo_num > com_num:
            print("down!")
        else:
            print("up!")


# 재도전 할건지 묻는 함수
def retry():
    retry_answer = input("재도전 하시겠습니까? y/n")
    if retry_answer == "y":
        total(level, life)
        return game(com_num, life)

    elif retry_answer == "n":
        total(level, life)
        exit()

    else:
        print("다시 입력해주세요")
        return retry()


def game(com_num, life):
    for i in range(1, life + 1):
        peo_num = int(input("숫자를 입력해주세요 : "))

        number_check(peo_num, com_num, life)

        print("\nlife = {}".format(life - i))


game(com_num, life)
