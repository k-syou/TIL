from collections import deque
# 상 우 하 좌
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
pipe_type = [
    # 해당 방향으로 갈 수 있는지를 기록
    [0, 0, 0, 0], # 빈칸
    [1, 1, 1, 1], # ┼
    [1, 0, 1, 0], # │
    [0, 1, 0, 1], # ─
    [1, 1, 0, 0], # └
    [0, 1, 1, 0], # ┌
    [0, 0, 1, 1], # ┐
    [1, 0, 0, 1], # ┘
]


def bfs(tunner_map, y, x, max_time):
    q = deque()
    q.append((y, x, 1))
    # 결과 값
    res_count = 1
    # 방문기록
    visited = [[False] * M for _ in range(N)]
    visited[y][x] = True

    while q:
        ty, tx, time = q.popleft()
        # 현재 위치의 파이프 타입
        c_pipe = pipe_type[tunner_map[ty][tx]]
        
        # 제한 시간을 넘긴경우
        if time >= max_time:
            continue
        
        for i in range(4):
            # 해당 방향으로 갈 수 없는 파이프인 경우
            if not c_pipe[i]:
                continue
            
            # 다음위치
            ny = ty + dy[i]
            nx = tx + dx[i]
            
            # 범위 초과
            if ny < 0 or nx < 0 or ny >= N or nx >= M:
                continue
            
            # 다음 위치 파이프 타입
            n_pipe = pipe_type[tunner_map[ny][nx]]
            if not n_pipe[(i + 2) % 4]:
                # 다음 위치 파이프에 접근이 불가능 한 경우
                continue
            
            # 이미 방문한 위치인 경우
            if visited[ny][nx]:
                continue
            visited[ny][nx] = True
            
            # 갈수 있는 통로 개수 추가
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
