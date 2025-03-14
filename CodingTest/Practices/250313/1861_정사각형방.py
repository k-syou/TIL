dy = (1, 0, -1, 0)
dx = (0, 1, 0, -1)
def dfs(y, x):
    if dp[y][x] != -1:
        return dp[y][x]
    dp[y][x] = 1
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if ny < 0 or nx < 0 or ny >= N or nx >= N:
            continue
        if board[ny][nx] - 1 != board[y][x]:
            continue
        dp[y][x] = max(dp[y][x], dfs(ny, nx) + 1)
    return dp[y][x]
        
        

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    board = [[*map(int, input().split())] for _ in range(N)]
    dp = [[-1] * N for _ in range(N)]
    max_v = -1
    num = 10 * 6 + 1
    for y in range(N):
        for x in range(N):
            if max_v < dfs(y, x):
                num = board[y][x]
                max_v = dp[y][x]
            elif max_v == dp[y][x] and num > board[y][x]:
                num = board[y][x]
    print(f"#{tc} {num} {max_v}")
