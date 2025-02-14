# 23528. 4873. [파이썬 S/W 문제해결 기본] 4일차 - 반복문자 지우기

for tc in range(1, int(input()) + 1):
    s = input()
    stack = []
    s_len = 0
    for i in range(len(s)):
        stack.append(s[i])
        s_len += 1
        if s_len > 1 and stack[-1] == stack[-2]:
            stack.pop()
            stack.pop()
            s_len -= 2
    print(f"#{tc} {len(stack)}")
