from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


def bfs(miro, N, sy, sx):
    q = deque()
    q.append((sy, sx, 0))  # 출발위치 및 거리값 초기화
    while q:  # 큐가 남아 있는 경우 실행
        ty, tx, dist = q.popleft()  # 제일 먼저들어온 정보 가져오기
        for i in range(4):  # 4방향 탐색
            ny = ty + dy[i]
            nx = tx + dx[i]
            if ny < 0 or nx < 0 or ny >= N or nx >= N:
                # 범위 초과
                continue
            if miro[ny][nx] == 3:
                # 도착한 경우
                return dist
            if miro[ny][nx] > 0:
                # 출발지거나 벽인 경우
                continue
            miro[ny][nx] = 1  # 이미 방문한경우 벽으로 변경(visited)
            q.append((ny, nx, dist + 1))  # 다음좌표 및 거리정보 큐에 추가
    # 도착할 수 없는 경우
    return 0


for tc in range(1, int(input()) + 1):
    N = int(input())
    miro = [[*map(int, input())] for _ in range(N)]

    # 출발지 찾기
    for y in range(N):
        for x in range(N):
            if miro[y][x] == 2:
                sy, sx = y, x
                break
    print(f"#{tc} {bfs(miro, N, sy, sx)}")
