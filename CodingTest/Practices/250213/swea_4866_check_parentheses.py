# 23527. 4866. [파이썬 S/W 문제해결 기본] 4일차 - 괄호검사
for tc in range(1, int(input()) + 1):
    s = input()
    stack = []
    res = 1
    for c in s:
        if c in ("(", "{"):
            stack.append(c)
        elif c == "}":
            if not stack or stack.pop() != "{":
                res = 0
                break
        elif c == ")":
            if not stack or stack.pop() != "(":
                res = 0
                break
    if stack:
        res = 0
    print(f"#{tc} {res}")
