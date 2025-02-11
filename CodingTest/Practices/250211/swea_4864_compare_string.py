T = int(input())
for tc in range(1, T + 1):
    s1 = input()
    s2 = input()

    temp = list(s2[: len(s1)])
    res = 0
    for i in range(len(s1), len(s2)):
        if s1 == "".join(temp):
            res = 1
            break
        temp.pop(0)
        temp.append(s2[i])
    print(f"#{tc} {res}")
