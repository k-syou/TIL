# 17144, 미세먼지 안녕!
t_dy = [0, -1, 0, 1]
b_dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]


def fine_dust_spreads(dust_loc):
    global room
    temp = [[0] * C for _ in range(R)]
    for y, x in dust_loc:
        f_dust = room[y][x] // 5
        if f_dust == 0:
            continue
        for i in range(4):
            ny = y + t_dy[i]
            nx = x + dx[i]
            if ny < 0 or nx < 0 or ny >= R or nx >= C:
                continue
            if room[ny][nx] == -1:
                continue
            temp[ny][nx] += f_dust
            room[y][x] -= f_dust
    for y in range(R):
        for x in range(C):
            room[y][x] += temp[y][x]


def air_purifier(curr_value, y, x, d, dy, dx):
    global room
    q = []
    q.append((y, x, d, curr_value))
    while q:
        ty, tx, td, value = q.pop()
        if room[ty][tx] == -1:
            return
        next_value = room[ty][tx]
        room[ty][tx] = value
        ny = ty + dy[td]
        nx = tx + dx[td]
        nd = td
        if ny < 0 or nx < 0 or ny >= R or nx >= C:
            nd = (nd + 1) % 4
            ny = ty + dy[nd]
            nx = tx + dx[nd]
        q.append((ny, nx, nd, next_value))


def get_dust_loc():
    dust_loc = []
    for y in range(R):
        for x in range(C):
            if room[y][x] > 0:
                dust_loc.append((y, x))
    return dust_loc


R, C, T = map(int, input().split())
room = [[*map(int, input().split())] for _ in range(R)]
curr_dust_loc = []
air_purifier_loc = []
for y in range(R):
    for x in range(C):
        if room[y][x] == -1:
            air_purifier_loc.append((y, x))
        elif room[y][x]:
            curr_dust_loc.append((y, x))

for t in range(T):
    fine_dust_spreads(curr_dust_loc)
    ty, tx = air_purifier_loc[0]
    by, bx = air_purifier_loc[1]
    air_purifier(0, ty, tx + 1, 0, t_dy, dx)
    air_purifier(0, by, bx + 1, 0, b_dy, dx)
    curr_dust_loc = get_dust_loc()


dust = sum(map(lambda loc: room[loc[0]][loc[1]], curr_dust_loc))
print(dust)

"""
7 8 20
0 0 0 0 0 0 0 9
0 0 0 0 3 0 0 8
-1 0 5 0 0 0 22 0
-1 8 0 0 0 0 0 0
0 0 0 0 0 10 43 0
0 0 5 0 15 0 0 0
0 0 40 0 0 0 20 0
"""
