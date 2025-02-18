ops = ["+", "-", "/", "*", "."]


def cal(op, a, b):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        return a // b


for tc in range(1, int(input()) + 1):
    s = input().split()
    res = 0
    stack = []
    for c in s:
        if c in ops:
            if c == ".":
                break
            elif len(stack) < 2:
                res = "error"
                break
            else:
                b, a = stack.pop(), stack.pop()
                stack.append(cal(c, a, b))
        else:
            stack.append(int(c))
    if len(stack) == 1 and res == 0:
        res = stack.pop()
    print(f"#{tc} {res}")
