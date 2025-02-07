from copy import deepcopy
from itertools import combinations


def get_arrow_shot(d):
    w = 1
    arrows = [[0, 0] for _ in range(d * 2 - 1)]
    for i in range(d * 2 - 1):
        if i + 1 <= d:
            arrows[i][0] = -(i + 1)
        else:
            arrows[i][0] = -(i - w)
            w += 1
    for j in range(d * 2 - 1):
        arrows[j][1] = j - (d - 1)

    return arrows


def play(arrows, archers, turn):
    global N, M, temp_defense_map
    shot_loc = set()
    for archer in archers:
        a_loc_x = archer
        a_loc_y = N - turn
        for dy, dx in arrows:
            ny = a_loc_y + dy
            nx = a_loc_x + dx
            if ny < 0 or ny >= N or nx < 0 or nx >= M:
                continue
            if temp_defense_map[ny][nx] == 0:
                continue
            shot_loc.add((ny, nx))
            break
    for y, x in shot_loc:
        temp_defense_map[y][x] = 0
    return len(shot_loc)


N, M, D = map(int, input().split())
defense_map = [[*map(int, input().split())] for _ in range(N)]
arrows = []

for d in range(1, D + 1):
    arrows.extend(get_arrow_shot(d))
result = 0

for archers in combinations(range(M), 3):
    kill_count = 0
    temp_defense_map = deepcopy(defense_map)
    for i in range(N):
        kill_count += play(arrows, archers, i)
    result = max(kill_count, result)

print(result)
