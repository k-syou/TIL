from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


def bfs(miro, N, sy, sx):
    q = deque()
    # queue 에 시작지점 추가
    q.append((sy, sx))
    while q:  # 큐가 비어있지 않으면 실행
        ty, tx = q.popleft()  # 먼저 들어온 좌표 가져오기
        for i in range(4):  # 4방향 검색
            ny = ty + dy[i]  # 다음 좌표 y(r)값
            nx = tx + dx[i]  # 다음 좌표 x(c)값
            if ny < 0 or nx < 0 or ny >= N or nx >= N:
                # 범위 초과
                continue
            if miro[ny][nx] == 3:
                # 도착한 경우
                return 1
            if miro[ny][nx] > 0:
                # 출발지 or 벽인 경우
                continue
            miro[ny][nx] = 1  # 이미 왔던길은 벽으로 변경(visited)
            q.append((ny, nx))  # 다음 위치 좌표 q에 추가
    # 도착지에 갈 수 없는 경우
    return 0


for _ in range(10):
    tc = int(input())
    N = 16
    miro = [[*map(int, input())] for _ in range(N)]

    # 출발 위치 찾기
    for y in range(N):
        for x in range(N):
            if miro[y][x] == 2:
                sy, sx = y, x
                break
    print(f"#{tc} {bfs(miro, N, sy, sx)}")
