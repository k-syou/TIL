# R, C, K = map(int, input().split())
# room = [[*map(int, input().split())] for _ in range(C)]
# W = int(input())
# wall_info = [[*map(int, input().split())] for _ in range(W)]


# # R : N | C : M | K : 온도
# R, C, K = 7, 8, 70
# room = [
#     [0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 4, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 5, 5, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 5, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 3, 0, 0, 0],
# ]
# W = 3
# wall_info = [[4, 4, 1], [5, 4, 0], [5, 6, 0]]
from pprint import pprint
from collections import *

# 상 우 하 좌
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
dh = [None, 1, 3, 0, 2]

R, C, K = map(int, input().split())
room = [[*map(int, input().split())] for _ in range(R)]
W = int(input())
wall_info = [[*map(int, input().split())] for _ in range(W)]

temperature = [[0] * C for _ in range(R)]
check_loc = []
heater_loc = []
wall_dict = defaultdict(set)
chocolate = 0

# 벽 위치 확인
for y, x, t in wall_info:
    wall_dict[(y - 1, x - 1)] |= {t}
    if t == 0:
        wall_dict[(y - 2, x - 1)] |= {2}
    else:
        wall_dict[(y - 1, x)] |= {3}

# 온도 확인할 위치 좌표와 온풍기의 좌표 찾기
for y in range(R):
    for x in range(C):
        if room[y][x] == 5:
            check_loc.append((y, x))
            continue
        if room[y][x]:
            heater_loc.append((y, x, room[y][x]))


def range_check(y, x):
    return 0 <= y < R and 0 <= x < C


def run_heater(heater_loc):
    global temperature

    def check(visited, d, w, ny, nx):
        return d not in w and range_check(ny, nx) and not visited[ny][nx]

    def dfs(visited, y, x, d, val):
        global temperature
        if val == 0:
            return
        # 바로 앞 확인
        ny = y + dy[d]
        nx = x + dx[d]
        if check(visited, d, wall_dict[(y, x)], ny, nx):
            temperature[ny][nx] += val
            visited[ny][nx] = 1
            dfs(visited, ny, nx, d, val - 1)

        # 양 옆 대각선 확인
        for i in (-1, 1):
            ty = y + dy[(d + i) % 4]
            tx = x + dx[(d + i) % 4]
            if check(visited, (d + i) % 4, wall_dict[(y, x)], ty, tx):
                ny = ty + dy[d]
                nx = tx + dx[d]
                if check(visited, d, wall_dict[(ty, tx)], ny, nx):
                    temperature[ny][nx] += val
                    visited[ny][nx] = 1
                    dfs(visited, ny, nx, d, val - 1)

    for y, x, v in heater_loc:
        d = dh[v]
        ny = y + dy[d]
        nx = x + dx[d]
        visited = [[0] * C for _ in range(R)]
        visited[ny][nx] = 1
        temperature[ny][nx] += 5
        dfs(visited, ny, nx, d, 4)


def temp_control():
    global temperature
    temp_matrix = [[0] * C for _ in range(R)]
    for y in range(R):
        for x in range(C):
            if temperature[y][x] <= 3:
                # 3이하의 온도는 옮겨질 일이 없음
                continue
            w = wall_dict[(y, x)]
            curr_temp = temperature[y][x]

            for i in range(4):
                if i in w:
                    continue
                ny = y + dy[i]
                nx = x + dx[i]
                if not range_check(ny, nx):
                    continue
                if curr_temp <= temperature[ny][nx]:
                    continue
                change_temp = (curr_temp - temperature[ny][nx]) // 4
                temp_matrix[ny][nx] += change_temp
                temp_matrix[y][x] -= change_temp

    for y in range(R):
        for x in range(C):
            temperature[y][x] += temp_matrix[y][x]
            if y == 0 or x == 0 or y == R - 1 or x == C - 1:
                temperature[y][x] -= 1 if temperature[y][x] > 0 else 0


def check_temp(check_loc):
    global temperature
    for y, x in check_loc:
        if temperature[y][x] < K:
            return True
    return False


while check_temp(check_loc) and chocolate < 101:
    run_heater(heater_loc)
    temp_control()
    chocolate += 1
print(chocolate)
