# 27453. 귀엽기만 한 게 아닌 한별 양

# 1. 벽(X)는 지나 갈 수 없다.
# 2. 바로 직전에 방문한 칸으로 돌아가지 않는다.
# 3. 최근지나온 3개 칸에 불상사의 개수가 K 초과이면 실패
# 4. 출발지(S) -> 도착지(H)
# 5. 가능한 경로 중 가장 짧은 길이 출력
# 6. 안전하게 귀가가 불가능 한 경우 -1

# BFS
# 좌표, 가중치(q), 이동거리
from collections import deque


def set_type(v):
    if v in 'SHX':
        return v
    return int(v)


def bfs(board):
    global N, M, K
    # 시작 위치 구하기
    sy = sx = -1
    for y in range(N):
        for x in range(M):
            if board[y][x] == 'S':
                sy, sx = y, x
                board[sy][sx] = 0
                break
        if sy != -1:
            break
    
    q = deque()
    q.append((sy, sx, -1, -1, deque(), 0, 0))
    # 지나온 길의 개수가 몇개일때 해당 방문 기록의 최소치가 몇인지 확인
    visited = [[[float('inf')] * 4 for _ in range(M)] for _ in range(N)]
    set_states = set()
    while q:
        ty, tx, py, px, prev_q, prev_tot, dist = q.popleft()
        for i in range(4):
            ny = ty + dy[i]
            nx = tx + dx[i]
            if ny < 0 or nx < 0 or ny >= N or nx >= M:
                continue  # 범위 초과
            if ny == py and nx == px:
                continue  # 바로 직전에 들린 곳
            value = board[ny][nx]
            if value == 'X':
                continue  # 벽
            if value == 'H':
                return dist + 1  # 집 도착한 경우
            lq = len(prev_q)
            if lq == 3:
                next_tot = prev_tot - prev_q[0] + value
                new_length = 3
            else:
                next_tot = prev_tot + value
                new_length = lq + 1
            
            if next_tot > K or next_tot > visited[ny][nx][new_length]:
                continue
                
            next_q = prev_q.copy()
            if lq == 3:
                next_q.popleft()
            next_q.append(value)
            if next_tot == visited[ny][nx][new_length]:
                state = (ny, nx, next_tot, tuple(next_q))
                if state in set_states:
                    continue
                set_states.add(state)
            visited[ny][nx][new_length] = next_tot
            q.append((ny, nx, ty, tx, next_q, next_tot, dist + 1))
            
    return -1


dy = (-1, 0, 1, 0)
dx = (0, 1, 0, -1)
N, M, K = map(int, input().split())
board = [[*map(set_type, input())] for _ in range(N)]
print(bfs(board))
