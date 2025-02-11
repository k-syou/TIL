T = int(input())


def calculate(x, n1, n2):
    if x == 0:
        return n1 + n2
    elif x == 1:
        return n1 - n2
    elif x == 2:
        return n1 * n2
    else:
        if n1 < 0:
            return -(-n1 // n2)
        else:
            return n1 // n2


def dfs(operators, numbers, idx, n):
    global min_v, max_v
    if idx == N:
        min_v = min(min_v, n)
        max_v = max(max_v, n)
        return
    for i in range(4):
        if operators[i] > 0:
            operators[i] -= 1
            next_num = calculate(i, n, numbers[idx])
            dfs(operators, numbers, idx + 1, next_num)
            operators[i] += 1


for tc in range(1, T + 1):
    N = int(input())
    operators = [*map(int, input().split())]  # + - * /
    numbers = [*map(int, input().split())]
    min_v = 9**12 + 1
    max_v = -(9**12) - 1
    dfs(operators, numbers, 1, numbers[0])
    # print(max_v, min_v)
    print(f"#{tc} {max_v - min_v}")
