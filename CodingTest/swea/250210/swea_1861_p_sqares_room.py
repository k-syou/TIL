import sys

sys.setrecursionlimit(10**7)
sys.stdin = open("input.txt", "r")

from collections import deque

T = int(input())
dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]


def dfs(rooms, sy, sx, room_num):
    global dp
    if dp[room_num] != 1:
        return dp[room_num]
    for i in range(4):
        ny = sy + dy[i]
        nx = sx + dx[i]
        if ny < 0 or ny >= N or nx < 0 or nx >= N:
            continue
        if rooms[ny][nx] != rooms[sy][sx] + 1:
            continue
        dp[room_num] = dfs(rooms, ny, nx, rooms[ny][nx]) + 1
    return dp[room_num]


result = []
for tc in range(1, T + 1):
    N = int(input())
    rooms = [[*map(int, input().split())] for _ in range(N)]
    dp = [1] * (N**2 + 1)
    length = 0
    for i in range(N):
        for j in range(N):
            dp[rooms[i][j]] = dfs(rooms, i, j, rooms[i][j])
            if length < dp[rooms[i][j]]:
                length = dp[rooms[i][j]]
    room_num = dp.index(length)
    result.append((tc, room_num, length))

for tc, room_num, length in result:
    print(f"#{tc} {room_num} {length}")
