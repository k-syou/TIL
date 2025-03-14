N = 10
grid = [[0] * N for _ in range(N)]
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
from collections import deque
def bfs(grid):
    q = deque()
    q.append((0, 0))
    visited = [[0] * N for _ in range(N)]
    visited[0][0] = 1
    w = 0
    while q:
        r, c = q.pop()
        # print(w, r, c)
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr < 0 or nc < 0 or nr >= N or nc >= N:
                continue
            if visited[nr][nc]:
                continue
            visited[nr][nc] = 1
            grid[nr][nc] = w + 1
            w += 1
            q.append((nr, nc))

bfs(grid)

for row in grid:
    print(*row)
    