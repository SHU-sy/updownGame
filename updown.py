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

# 초기 life 개수 설정
initial_life = 5

# 전역 level 설정
level = 1


# 현재 위치
def total(life, level):
    print("life : {}".format(life))
    print("level : {}".format(level))


# 입력한 숫자 검증
def number_check(peo_num, com_num, life):
    global level  # 전역 level 변수 사용
    if peo_num == com_num:  # 추측한 숫자가 맞았을 경우
        print("성공!!!")
        level += 1
        return retry(initial_life)

    elif life == 0:  # life 를 다 잃었을 경우
        print("실패!!!")
        return retry(initial_life)

    else:  # 추측한 숫자가 틀렸을 경우
        if peo_num > com_num:
            print("down!")
        else:
            print("up!")
        life -= 1
        if life == 0:
            print("실패!!!")
            return retry(initial_life)
        print("\nlife = {}".format(life))
        return life


# 재도전 할건지 묻는 함수
def retry(life):
    retry_answer = input("재도전 하시겠습니까? y/n: ")
    if retry_answer == "y":
        total(life, level)
        return game(life)

    elif retry_answer == "n":
        total(life, level)
        exit()

    else:
        print("다시 입력해주세요")
        return retry(initial_life)


# 게임 함수
def game(life):
    com_num = random.randrange(1, 101)  # 새로운 게임 시작 시 숫자 생성
    while life > 0:
        peo_num = int(input("숫자를 입력해주세요: "))
        life = number_check(peo_num, com_num, life)


game(initial_life)
