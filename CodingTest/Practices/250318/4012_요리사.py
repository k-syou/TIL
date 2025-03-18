def taste_diff(A, B):
    tot_a = 0
    tot_b = 0
    for i in range(N//2):
        for j in range(i+1, N//2):
            tot_a += taste[A[i]][A[j]]
            tot_b += taste[B[i]][B[j]]
    return abs(tot_a - tot_b)


def backtrack(idx, cnt, type):
    global res
    if cnt == N // 2:
        A = type
        B = []
        for i in range(N):
            if i not in type:
                B.append(i)
        res = min(res, taste_diff(A, B))
        return
    for i in range(idx+1, N):
        type.append(i)
        backtrack(i, cnt + 1, type)
        type.pop()


T = int(input()) + 1
for tc in range(1, T):
    N = int(input())
    S = [[*map(int, input().split())] for _ in range(N)]
    taste = {i:[0] * N for i in range(N)}
    for i in range(N):
        for j in range(i + 1, N):
            taste[i][j] += S[i][j] + S[j][i]
    res = float('inf')
    backtrack(-1, 0, [])
    print(f"#{tc} {res}")