N = int(input())
result = []

# 초반 반복
for i in range(N - 1):
    if i == 0:
        text = "*" * N + " " * (1 + 2 * (N - 2)) + "*" * N
    else:
        text = (
            " " * i
            + "*"
            + " " * (N - 2)
            + "*"
            + " " * (1 + 2 * (N - 2 - i))
            + "*"
            + " " * (N - 2)
            + "*"
        )
    result.append(text)

# 중간줄
text = " " * (N - 1) + "*" + " " * (N - 2) + "*" + " " * (N - 2) + "*"
result.append(text)

# 마지막 반복
for i in range(N - 2, -1, -1):
    if i == 0:
        text = "*" * N + " " * (1 + 2 * (N - 2)) + "*" * N
    else:
        text = (
            " " * i
            + "*"
            + " " * (N - 2)
            + "*"
            + " " * (1 + 2 * (N - 2 - i))
            + "*"
            + " " * (N - 2)
            + "*"
        )
    result.append(text)

print(*result, sep="\n")
