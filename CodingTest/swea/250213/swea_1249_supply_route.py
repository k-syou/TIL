# 1249. [S/W 문제해결 응용] 4일차 - 보급로
import heapq

dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]


def dijkstra(N, grid, sy, sx, ey, ex):
    # 우선순위 큐 heapq 를 활용한 최단 시간 찾기
    # hq = [(시간, 행위치, 열위치), ...]
    hq = []
    heapq.heappush(hq, (0, sy, sx))

    # visited = 가장 짧은 방문 기록
    visited = [[float("inf")] * N for _ in range(N)]
    visited[sy][sx] = 0

    while hq:
        td, ty, tx = heapq.heappop(hq)
        if ty == ey and tx == ex:
            # 가장 짧은 시간으로 도착하기 때문에 바로 return
            return td
        for i in range(4):
            ny = ty + dy[i]
            nx = tx + dx[i]
            if ny < 0 or nx < 0 or ny >= N or nx >= N:
                continue
            # nd = 다음 위치까지의 복구 시간
            # grid[ny][nx] 가 도로의 깊이 이므로 도로의 깊이만큼 시간이 누적됨
            nd = td + grid[ny][nx]
            if visited[ny][nx] <= nd:
                # 다음 위치까지의 시간이 이미 방문한 기록보다 긴 경우 스킵
                continue
            visited[ny][nx] = nd
            heapq.heappush(hq, (nd, ny, nx))


for tc in range(1, int(input()) + 1):
    N = int(input())
    grid = [[*map(int, input())] for _ in range(N)]
    print(f"#{tc} {dijkstra(N, grid, 0, 0, N - 1, N - 1)}")
