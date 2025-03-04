n = int(input())
matrixs = [[*map(int, input().split())] for _ in range(n)]
dp = [[0, 0] for _ in range(n)]

if n > 1:
    dp[1] = [
        matrixs[0][0] * matrixs[0][1] * matrixs[1][1],
        matrixs[0][0] * matrixs[0][1] * matrixs[1][1],
    ]
if n > 2:
    dp[2] = [
        dp[1][0] + matrixs[0][0] * matrixs[2][0] * matrixs[2][1],
        matrixs[0][0] * matrixs[0][1] * matrixs[2][1]
        + matrixs[1][0] * matrixs[2][0] * matrixs[2][1],
    ]

for i in range(3, n):
    # ab_c =
    pass

print(min(dp[n - 1]))
