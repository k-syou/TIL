dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]


def dfs(miro, visited, y, x):
    if miro[y][x] == 3:
        return 1
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if ny < 0 or nx < 0 or ny >= N or nx >= N:
            continue
        if visited[ny][nx]:
            continue
        visited[ny][nx] = 1
        if miro[ny][nx] == 1:
            continue
        res = dfs(miro, visited, ny, nx)
        if res:
            return res
    return 0


for tc in range(1, int(input()) + 1):
    N = int(input())
    miro = [[*map(int, input())] for _ in range(N)]
    sy, sx = -1, -1
    for x in range(N):
        if miro[N - 1][x] == 2:
            sy, sx = N - 1, x
            break
    visited = [[0] * N for _ in range(N)]
    visited[sy][sx] = 1
    print(f"#{tc} {dfs(miro, visited, sy, sx)}")
