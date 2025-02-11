# https://swexpertacademy.com/main/solvingProblem/solvingProblem.do
T = int(input())
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def dfs(y, x, length, construction_count, mountain, visited):
    global max_length
    max_length = max(max_length, length)
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if ny < 0 or nx < 0 or ny >= N or nx >= N:
            continue
        if not visited[ny][nx][construction_count]:
            continue
        if mountain[y][x] <= mountain[ny][nx]:
            if construction_count and mountain[y][x] > mountain[ny][nx] - K:
                tmp = mountain[ny][nx]
                mountain[ny][nx] = mountain[y][x] - 1
                visited[ny][nx][0] = False
                dfs(ny, nx, length + 1, 0, mountain, visited)
                visited[ny][nx][0] = True
                mountain[ny][nx] = tmp
            continue
        visited[ny][nx][construction_count] = False
        dfs(ny, nx, length + 1, construction_count, mountain, visited)
        visited[ny][nx][construction_count] = True


for tc in range(1, T + 1):
    N, K = map(int, input().split())
    mountain = [[*map(int, input().split())] for _ in range(N)]
    max_v = 0
    start_loc = []
    for y in range(N):
        if max_v < max(mountain[y]):
            start_loc = []
            max_v = max(mountain[y])
        for x in range(N):
            if max_v == mountain[y][x]:
                start_loc.append((y, x))

    max_length = -1
    for y, x in start_loc:
        visited = [[[True, True] for _ in range(N)] for _ in range(N)]
        visited[y][x][1] = False
        visited[y][x][0] = False
        dfs(y, x, 1, 1, mountain, visited)

    print(f"#{tc} {max_length}")

"""
1
4 4
8 3 9 5
4 6 8 5
8 1 5 1
4 9 5 5
"""
