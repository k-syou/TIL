# 5432. 쇠막대기 자르기
for tc in range(1, int(input()) + 1):
    s = input()
    s_len = 0  # 누적된 파이프 개수
    tot = 0  # 잘라진 파이프의 총 개수
    for i in range(len(s)):
        if s[i] == "(":  # 파이프의 시작점인 경우
            s_len += 1  # 파이프 개수 누적
        elif s[i] == ")" and s_len:
            s_len -= 1  # 누적 파이프 개수 감소
            if s[i - 1] == "(":  # 레이저인 경우
                tot += s_len  # 현재 누적된 파이프 개수만큼 누적
            else:
                tot += 1  # 파이프가 끝날때, 파이프 개수 + 1

    print(f"#{tc} {tot}")
