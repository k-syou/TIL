from collections import deque
import heapq

def set_type(v):
    if v in 'SHX':
        return v
    return int(v)


def get_sum(env, l):
    result = 0
    while l > 0:
        tmp = env >> 4 * (l - 1)
        result += tmp
        env -= tmp << 4 * (l - 1)
        l -= 1
    return result


def env_add(env, v, l):
    if l == 0:
        return v
    if l == 3:
        tmp = (env >> 8) << 8
        env -= tmp
    env = env << 4
    env += v
    return env


def bfs(board):
    global N, M, K
    # 시작 위치 구하기
    sy = sx = -1
    for y in range(N):
        for x in range(M):
            if board[y][x] == 'S':
                sy, sx = y, x
                board[sy][sx] = 'X'
                break
        if sy != -1:
            break
    hq = []
    q = deque()
    # q.append((sy, sx, -1, -1, deque(), 0, 0))
    heapq.heappush(hq, (0, 0, 0, (sy, sx), (-1, -1)))
    # q.append(((sy, sx), (-1, -1), 0, 0, 0))
    # 지나온 길의 개수가 몇개일때 해당 방문 기록의 최소치가 몇인지 확인
    visited = [[[float('inf')] * 4 for _ in range(M)] for _ in range(N)]
    sets = set()
    while hq:
        # start, prev, env, env_len, dist = q.popleft()
        dist, env, env_len, start, prev = heapq.heappop(hq)
        env = -env
        dist = dist
        ty, tx = start
        py, px = prev
        # print(env, dist)
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
            new_env = env_add(env, value, env_len)
            if env_len == 3:
                new_len = 3
                next_tot = get_sum(new_env, 3)
            else:
                new_len = env_len + 1
                next_tot = get_sum(new_env, new_len)
            
            if next_tot > K or next_tot > visited[ny][nx][new_len]:
                continue
            
            state = (ny, nx, start, new_env)
            if next_tot == visited[ny][nx][new_len] and state in sets:
                continue
            sets |= {state}
            visited[ny][nx][new_len] = next_tot
            # q.append(((ny, nx), start, new_env, new_len, dist + 1))
            heapq.heappush(hq, (dist + 1, -new_env, new_len, (ny, nx), start))
    return -1


import sys

input = sys.stdin.readline
dy = (-1, 0, 1, 0)
dx = (0, 1, 0, -1)
N, M, K = map(int, input().split())
board = [[*map(set_type, input().strip())] for _ in range(N)]
print(bfs(board))
