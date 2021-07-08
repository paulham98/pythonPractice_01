import random


def generate_numbers():
    numbers = []
    num = list(range(1, 10))
    for i in range(0, 3):
        numbers.append(num.pop(num.index(random.choice(num))))

    print("0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다.\n")
    return numbers


def take_guess():
    print("숫자 3개를 하나씩 차례대로 입력하세요.")
    new_guess = []
    guess = 1
    while len(new_guess) < 3:
        a = input(f"{guess}번째 숫자를 입력하세요:")
        if int(a) >= 10:
            print("범위를 벗어나는 숫자입니다. 다시 입력하세요.")
            a = input(f"{guess}번째 숫자를 입력하세요: ")
        for j in range(len(new_guess)):
            if new_guess[j] == a:
                print("중복된 숫자입니다. 다시 입력하세요.")
                a = input(f"{guess}번째 숫자를 입력하세요: ")
        new_guess.append(int(a))
        guess += 1

    return new_guess


def get_score(guess, solution):
    strike_count = 0
    ball_count = 0
    for i in range(len(guess)):
        for j in range(len(solution)):
            if guess[i] == solution[j] and i == j:
                strike_count += 1
                continue
            elif guess[i] == solution[j]:
                ball_count += 1
    return strike_count, ball_count


ANSWER = generate_numbers()
tries = 1
while True:
    s, b = get_score(take_guess(), ANSWER)
    if s == 3 and b == 0:
        print("축하합니다. {}번 만에 숫자 3개의 값과 위치를 모두 맞추셨습니다.".format(tries))
        break
    else:
        print(f"{s}S {b}B")
        tries += 1


"""
# 테스트
s_1, b_1 = get_score([7, 2, 6], [7, 2, 6])
print(f"{s_1}S, {b_1}B")

s_2, b_2 = get_score([7, 2, 4], [2, 4, 7])
print(s_2, b_2)

s_3, b_3 = get_score([0, 4, 7], [2, 4, 7])
print(s_3, b_3)

s_4, b_4 = get_score([2, 4, 7], [2, 4, 7])
print(s_4, b_4)


# print(generate_numbers())
# print(take_guess())
"""
