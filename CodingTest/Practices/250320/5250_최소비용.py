import heapq

T = int(input()) + 1
dr = (-1, 0, 1, 0)
dc = (0, 1, 0, -1)


def dijkstra(board):
    hq = [(0, 0, 0)]
    visited = [[0] * N for _ in range(N)]
    visited[0][0] = 1
    while hq:
        dist, r, c = heapq.heappop(hq)
        if r == N-1 and c == N-1:
            return dist
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr < 0 or nc < 0 or nr >= N or nc >= N:
                continue
            if visited[nr][nc]:
                continue
            visited[nr][nc] = 1
            diff = 1
            if board[r][c] < board[nr][nc]:
                diff += board[nr][nc] + board[r][c]
            heapq.heappush(hq, (dist + diff, nr, nc))


for tc in range(1, T):
    N = int(input())
    board = [[*map(int, input().split())] for _ in range(N)]
    print(f"#{tc} {dijkstra(board)}")
