# 23469. 4865. [파이썬 S/W 문제해결 기본] 3일차 - 글자수
for tc in range(1, int(input()) + 1):
    str1 = input()
    str2 = input()
    res = 0
    for s in set(str1):
        cnt = 0
        for s2 in str2:
            if s == s2:
                cnt += 1
        res = max(res, cnt)
    print(f"#{tc} {res}")
