from random import randint


def generate_numbers(n):
    li = list()
    for i in range(0, n):
        gn = randint(1, 45)
        li.append(gn)
        li.sort()
    return li


def draw_winning_numbers():
    bonus = randint(1, 45)
    li = generate_numbers(6)
    li.append(bonus)
    return li


def count_matching_numbers(list_1, list_2):
    cnt = 0
    for i in range(len(list_1)):
        for j in range(len(list_2) - 1):
            if list_1[i] == list_2[j]:
                cnt += 1
    return cnt


def check(numbers, winning_numbers):
    # 코드를 작성하세요.
    for i in range(len(numbers)):
        if numbers[i] == winning_numbers[6] and count_matching_numbers(numbers, winning_numbers) == 5:
            return 50000000
    if count_matching_numbers(numbers, winning_numbers) == 6:
        return 1000000000
    elif count_matching_numbers(numbers, winning_numbers) == 5:
        return 1000000
    elif count_matching_numbers(numbers, winning_numbers) == 4:
        return 50000
    elif count_matching_numbers(numbers, winning_numbers) == 3:
        return 5000


# 테스트
# print(draw_winning_numbers())
# print(count_matching_numbers([2, 7, 11, 14, 25, 40], [2, 11, 13, 14, 30, 35]))
# print(count_matching_numbers([2, 7, 11, 14, 25, 40], [14]))
print(check([2, 4, 11, 14, 25, 40], [4, 12, 14, 28, 40, 41, 6]))
print(check([2, 4, 11, 14, 25, 40], [2, 4, 10, 11, 14, 40, 25]))
