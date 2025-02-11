from collections import deque, defaultdict


wall = [[2, 3, 1, 0], [1, 3, 0, 2], [3, 2, 0, 1], [2, 0, 3, 1], [2, 3, 0, 1]]


def play(game_board, sy, sx, direction):
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    result = 0
    q = deque()
    q.append((sy, sx, direction))
    first = True
    while q:
        # 현재 위치, 방향
        ty, tx, td = q.popleft()
        # 첫 위치로 온경우
        if ty == sy and tx == sx:
            if first:  # 첫 수행인 경우
                first = False
            else:  # 종료
                return result
        # 다음 위치 방향
        ny = ty + dy[td]
        nx = tx + dx[td]
        # 벽인 경우
        if ny < 0 or nx < 0 or ny >= N or nx >= N:
            result += 1
            nd = (td + 2) % 4
            q.append((ny, nx, nd))
            continue
        # 블랙홀(-1)
        if game_board[ny][nx] == -1:
            return result
        # 길(0)인 경우
        if game_board[ny][nx] == 0:
            q.append((ny, nx, td))
            continue
        # 벽(1 ~ 5)인 경우
        if game_board[ny][nx] <= 5:
            result += 1
            nd = wall[game_board[ny][nx] - 1][td]
            q.append((ny, nx, nd))
            continue
        # 웜홀을 만난 경우
        ny, nx = wormhole_loc[(ny, nx)]
        q.append((ny, nx, td))
    return 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    game_board = [[*map(int, input().split())] for _ in range(N)]
    wormhole = defaultdict(list)
    for y in range(N):
        for x in range(N):
            if game_board[y][x] >= 6:
                wormhole[game_board[y][x]].append((y, x))

    wormhole_loc = {}
    for value in dict(wormhole).values():
        wormhole_loc[value[0]] = value[1]
        wormhole_loc[value[1]] = value[0]

    result = 0
    for y in range(N):
        for x in range(N):
            if game_board[y][x] == 0:
                for i in range(4):
                    result = max(result, play(game_board, y, x, i))
    print(f"#{tc} {result}")
