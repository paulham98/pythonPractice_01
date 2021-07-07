import random

with open("vocabulary.txt", "r") as file:
    lines = file.readlines()
    problems = {}
    i = 0
    for line in lines:
        a = line.strip().split(": ")
        problems[i] = a
        # print(problems[i][0])
        i += 1
    for x in range(len(problems)):
        a = random.randint(0, len(problems) - 1)
        print(problems[a][0] + ": ", end='')
        ans = input()
        if ans == str(problems[a][1]):
            print("맞았습니다!")
        elif ans == "q":
            break
        else:
            print(f"아쉽습니다. 정답은 '{problems[a][1]}' 입니다.")
