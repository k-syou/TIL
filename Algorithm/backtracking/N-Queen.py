def promising(dp, i):
    for j in range(i):
        if dp[j] == dp[i] or abs(dp[j] - dp[i]) == i - j:
            return False
    return True


def n_queen(n, i):
    global queen, res
    if n == i:
        res += 1
        return
    for j in range(n):
        queen[i] = j
        if promising(queen, i):
            n_queen(n, i + 1)


N = 10
queen = [-1] * N
res = 0
n_queen(N, 0)
print(res)