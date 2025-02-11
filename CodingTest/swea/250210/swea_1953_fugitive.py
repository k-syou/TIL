from collections import deque

# 상 우 하 좌
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
pipe_type = [
    [0, 0, 0, 0],  # x
    [1, 1, 1, 1],  # +
    [1, 0, 1, 0],  # |
    [0, 1, 0, 1],  # -
    [1, 1, 0, 0],  # ㄴ
    [0, 1, 1, 0],  # ◤
    [0, 0, 1, 1],  # ㄱ
    [1, 0, 0, 1],  # ◢
]


def bfs(tunner_map, y, x, max_time):
    q = deque()
    q.append((y, x, 1))
    res_count = 1
    visited = [[False] * M for _ in range(N)]
    visited[y][x] = True

    while q:
        ty, tx, time = q.popleft()
        c_pipe = pipe_type[tunner_map[ty][tx]]
        if time >= max_time:
            continue
        for i in range(4):
            if not c_pipe[i]:
                continue
            ny = ty + dy[i]
            nx = tx + dx[i]
            if ny < 0 or nx < 0 or ny >= N or nx >= M:
                continue
            a_pipe = pipe_type[tunner_map[ny][nx]]
            if not a_pipe[(i + 2) % 4]:
                continue
            if visited[ny][nx]:
                continue
            visited[ny][nx] = True
            res_count += 1
            q.append((ny, nx, time + 1))

    return res_count


T = int(input())
for tc in range(1, T + 1):
    N, M, Y, X, L = map(int, input().split())
    tunner_map = [[*map(int, input().split())] for _ in range(N)]
    print(f"#{tc} {bfs(tunner_map, Y, X, L)}")


# 2
# 5 6 2 1 3
# 0 0 5 3 6 0
# 0 0 2 0 2 0
# 3 3 1 3 7 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 5 6 2 2 6
# 3 0 0 0 0 3
# 2 0 0 0 0 6
# 1 3 1 1 3 1
# 2 0 2 0 0 2
# 0 0 4 3 1 1
