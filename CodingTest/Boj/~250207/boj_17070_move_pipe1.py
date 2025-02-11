import sys
from collections import deque

sys.setrecursionlimit(10**7)

N = int(input())

# 대각선, 가로, 세로
dy = [1, 0, 1]
dx = [1, 1, 0]
direction_move = [[0, 1, 2], [0, 1], [0, 2]]

matrix = [[*map(int, input().split())] for _ in range(N)]

# def bfs(y, x, d):
#     q = deque()
#     q.append((y, x, d))
#     result = 0
#     while q:
#         ty, tx, td = q.popleft()
#         if ty == tx == N - 1:
#             result += 1
#             continue
#         for i in direction_move[td]:
#             ny = ty + dy[i]
#             nx = tx + dx[i]
#             if ny < 0 or ny >= N or nx < 0 or nx >= N:
#                 continue
#             if matrix[ny][nx]:
#                 continue
#             if i == 0 and (matrix[ny - 1][nx] or matrix[ny][nx - 1]):
#                 continue
#             q.append((ny, nx, i))
#     return result
#
#
# print(bfs(0, 1, 1))

result = 0
visited = [[[-1, -1, -1] for _ in range(N)] for _ in range(N)]


def dfs(n, y, x, direction):
    global result, visited
    if visited[y][x][direction] != -1:
        result += visited[y][x][direction]
        return
    tmp = result
    if y == x == n - 1:
        result += 1
        return
    for i in direction_move[direction]:
        ny = y + dy[i]
        nx = x + dx[i]
        if ny < 0 or ny >= n or nx < 0 or nx >= n:
            continue
        if matrix[ny][nx]:
            continue
        if i == 0 and (matrix[ny - 1][nx] or matrix[ny][nx - 1]):
            continue
        dfs(n, ny, nx, i)

    visited[y][x][direction] = result - tmp


dfs(N, 0, 1, 1)
print(result)

"""
16
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
"""
