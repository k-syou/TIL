from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]


def search_cust_bfs(y, x, grid):
    # 가장 거리가 가까운 손님 찾기
    q = deque()
    q.append((y, x, 0))
    visited = [[0] * N for _ in range(N)]
    visited[y][x] = 1
    dist = 10**5
    loc = []

    while q:
        ty, tx, td = q.popleft()
        if td >= dist:
            continue
        for i in range(4):
            ny = ty + dy[i]
            nx = tx + dx[i]
            if ny < 0 or nx < 0 or ny >= N or nx >= N:
                continue
            if visited[ny][nx]:
                continue
            visited[ny][nx] = 1
            if grid[ny][nx] == 1:
                continue
            if grid[ny][nx] > 0:
                loc.append((ny, nx))
                dist = td + 1
                continue

            q.append((ny, nx, td + 1))
    if loc:
        return *sorted(loc)[0], dist
    else:
        return -1, -1, -1


def search_goal_bfs(sy, sx, gy, gx, grid):
    # 해당 손님의 도착지 찾기
    q = deque()
    q.append((sy, sx, 0))
    visited = [[0] * N for _ in range(N)]
    visited[sy][sx] = 1

    while q:
        ty, tx, td = q.popleft()
        if ty == gy and tx == gx:
            return td
        for i in range(4):
            ny = ty + dy[i]
            nx = tx + dx[i]
            if ny < 0 or nx < 0 or ny >= N or nx >= N:
                continue
            if visited[ny][nx]:
                continue
            visited[ny][nx] = 1
            if grid[ny][nx] == 1:
                continue
            q.append((ny, nx, td + 1))
    return -1


N, M, oil = map(int, input().split())
grid = [[*map(int, input().split())] for _ in range(N)]

sy, sx = map(lambda x: int(x) - 1, input().split())

customer = []
goal = [None, None]

for i in range(M):
    cy, cx, gy, gx = map(lambda x: int(x) - 1, input().split())
    goal.append((gy, gx))
    grid[cy][cx] = i + 2

# from pprint import pprint

# print("------------------")
# pprint(grid)
# print("------------------")

for _ in range(M):
    # 가장 가까운 손님 위치 및 거리
    if grid[sy][sx] > 0:
        cy, cx, dist = sy, sx, 0
    else:
        cy, cx, dist = search_cust_bfs(sy, sx, grid)
    # print(f"{sy}, {sx} => {cy}, {cx} : {dist}")
    if cy == -1 or oil - dist < 0:  # 손님을 찾지 못했거나 연료가 부족한 경우
        oil = -1
        break
    oil -= dist

    # 도착지 까지의 거리
    goal_idx = grid[cy][cx]
    goal_loc = goal[goal_idx]
    grid[cy][cx] = 0

    dist = search_goal_bfs(cy, cx, *goal_loc, grid)
    # print(f"{cy}, {cx} => {goal_loc[0]}, {goal_loc[1]} : {dist}")
    if dist < 0 or oil - dist < 0:
        # 도착지를 찾지 못했거나 도착지 까지 가는 연료가 부족한 경우
        oil = -1
        break

    sy, sx = goal_loc
    oil += dist

print(oil)
