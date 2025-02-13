# 4789. 성공적인 공연 기획

for tc in range(1, int(input()) + 1):
    s = input()
    N = len(s)
    tot = 0  # 박수를 치고있는 사람들 수의 합
    res = 0  # 추가적으로 박수를 쳐야할 사람의 수
    for i in range(N):  # 박수를 칠수있는 최소 인원(i)
        n = int(s[i])  # 박수를 칠 사람 수
        if not n:  # n == 0
            continue

        if i <= tot:  # 최소 박수 인원 <= 박수를 총 치고있는 인원
            tot += n  # 박수 치고있는 사람들에 박수를 칠 사람들의 수를 더함
        else:
            res += i - tot  # 추가 인원 투입
            tot = i + n  # 박수 치고있는 사람 수 변경
    print(f"#{tc} {res}")
