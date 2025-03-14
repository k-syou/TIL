dr = (0, 1)
dc = (1, 0)


def dfs(r, c, tot):
    global dp
    for i in range(2):
        nr = r + dr[i]
        nc = c + dc[i]
        if nr >= N or nc >= N:
            continue
        nv = board[nr][nc]
        if dp[nr][nc] <= tot + nv:
            continue
        dp[nr][nc] = tot + nv
        dfs(nr, nc, dp[nr][nc])

def dfs(r, c):
    global dp
    if dp[r][c]:
        return dp[r][c]
    dp[r][c] = board[r][c]
    if r == 0 and c == 0:
        return dp[r][c]
    min_v = INF
    for i in range(2):
        nr = r - dr[i]
        nc = c - dc[i]
        if nr < 0 or nc < 0:
            continue
        min_v = min(min_v, dfs(nr, nc))
    dp[r][c] += min_v
    return dp[r][c]

T = int(input())
INF = float('inf')
for tc in range(1, T + 1):
    N = int(input())
    board = [[*map(int, input().split())] for _ in range(N)]
    # dp = [[INF] * N for _ in range(N)]
    dp = [[0] * N for _ in range(N)]
    # dfs(0, 0, board[0][0])
    
    # print(f"#{tc} {dp[N-1][N-1]}")
    print(f"#{tc} {dfs(N - 1, N - 1)}")


def dfs(r, c):
    global dp
    if dp[r][c]:
        return dp[r][c]
    dp[r][c] = board[r][c]
    if r == 0 and c == 0:
        return dp[r][c]
    min_v = INF
    for i in range(2):
        nr = r - dr[i]
        nc = c - dc[i]
        if nr < 0 or nc < 0:
            continue
        min_v = min(min_v, dfs(nr, nc))
    dp[r][c] += min_v
    return dp[r][c]

T = int(input())
INF = float('inf')
for tc in range(1, T + 1):
    N = int(input())
    board = [[*map(int, input().split())] for _ in range(N)]
    dp = [[0] * N for _ in range(N)]
    print(f"#{tc} {dfs(N - 1, N - 1)}")

