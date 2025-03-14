def dfs(i, tot, depth):
    global visited, result
    if depth == N:
        result = min(result, tot + board[i][0])
        return
    visited[i] = 1
    for j in range(N):
        if visited[j]:
            continue
        dfs(j, tot + board[i][j], depth + 1)
    visited[i] = 0

T = int(input())

for tc in range(1, T + 1):
    N = int(input())  # 3 <= N <= 10
    board = [[*map(int, input().split())] for _ in range(N)]
    visited = [0] * N
    result = float('inf')
    dfs(0, 0, 1)
    print(f"#{tc} {result}")