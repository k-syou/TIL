dy = [1, 1, -1, -1]
dx = [1, -1, -1, 1]


def dfs(y, x, d, dessert: set, cnt):
    global res, sy, sx
    # 현재 위치의 디저트 추가
    tdessert = dessert.copy()
    tdessert |= {cafe_map[y][x]}
    cnt += 1

    # print(y, x, d, tdessert)
    # 가던 방향으로 갈때
    ny = y + dy[d]
    nx = x + dx[d]
    if ny == sy and nx == sx:  # 원래 자리로 돌아온 경우
        # print("정답 :", cnt)
        res = max(res, cnt)
        return
    if 0 <= ny < N and 0 <= nx < N and cafe_map[ny][nx] not in tdessert:
        dfs(ny, nx, d, tdessert, cnt)

    # 방향 전환
    nd = d + 1
    if nd == 4:
        return
    ny = y + dy[nd]
    nx = x + dx[nd]
    if ny == sy and nx == sx:  # 원래 자리로 돌아온 경우
        # print("정답(회전) :", cnt)
        res = max(res, cnt)
        return
    if 0 <= ny < N and 0 <= nx < N and cafe_map[ny][nx] not in tdessert:
        dfs(ny, nx, nd, tdessert, cnt)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    cafe_map = [[*map(int, input().split())] for _ in range(N)]
    res = -1
    for sy in range(N - 2):
        for sx in range(1, N - 1):
            dfs(sy, sx, 0, set(), 0)

    print(f"#{tc} {res}")

"""
1
5
8 2 9 6 6
1 9 3 3 4
8 2 3 3 6
4 3 4 4 9
7 4 6 3 5
"""
