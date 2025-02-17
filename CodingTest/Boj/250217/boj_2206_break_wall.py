import heapq

N, M = map(int, input().split())
grid = [[*map(int, input())] for _ in range(N)]
dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]


def dijkstra(grid):
    q = []
    q.append((1, 1, 0, 0))
    visited = [[[10**7] * 2 for _ in range(M)] for _ in range(N)]
    visited[0][0][1] = 0
    while q:
        tdist, tdrill, ty, tx = heapq.heappop(q)
        if ty == N - 1 and tx == M - 1:
            return tdist
        for i in range(4):
            ny = ty + dy[i]
            nx = tx + dx[i]
            if ny < 0 or nx < 0 or ny >= N or nx >= M:
                continue
            if grid[ny][nx] == 1:
                if tdrill == 0:
                    continue
                if visited[ny][nx][tdrill - 1] > tdist + 1:
                    visited[ny][nx][tdrill - 1] = tdist + 1
                    heapq.heappush(q, (tdist + 1, tdrill - 1, ny, nx))
            else:
                if visited[ny][nx][tdrill] > tdist + 1:
                    visited[ny][nx][tdrill] = tdist + 1
                    heapq.heappush(q, (tdist + 1, tdrill, ny, nx))
    return -1


print(dijkstra(grid))
