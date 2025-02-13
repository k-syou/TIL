# 1767. [SW Test 샘플문제] 프로세서 연결하기
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


def connected(y, x, d, cnt):
    global visited
    if visited[y][x]:
        return 0
    ny = y + dy[d]
    nx = x + dx[d]
    if ny < 0 or nx < 0 or ny >= N or nx >= N:
        visited[y][x] = 1
        return cnt
    line = connected(ny, nx, d, cnt + 1)
    if line:
        visited[y][x] = 1
    else:
        visited[y][x] = 0
    return line


def unconnected(y, x, d):
    global visited
    ny = y + dy[d]
    nx = x + dx[d]
    if ny < 0 or nx < 0 or ny >= N or nx >= N:
        return
    visited[y][x] = 0
    unconnected(ny, nx, d)


def backtrack(cores, C, i, lines):
    global res, visited
    if res <= lines:
        return
    if i >= C:
        print(lines)
        for row in visited:
            print(*row)
        res = min(res, lines)
        return
    y, x = cores[i]
    for d in range(4):
        ny = y + dy[d]
        nx = x + dx[d]
        if ny < 0 or nx < 0 or ny >= N or nx >= N:
            continue
        lines_cnt = connected(ny, nx, d, 1)
        if i == 1:
            print("-------------")
            for row in visited:
                print(*row)
        if lines_cnt:
            backtrack(cores, C, i + 1, lines + lines_cnt)
            unconnected(ny, nx, d)


for tc in range(1, int(input()) + 1):
    N = int(input())
    processor = [[*map(int, input().split())] for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    cores = []
    for y in range(N):
        for x in range(N):
            if processor[y][x] == 1:
                visited[y][x] = 3
                if 0 < y < N - 1 and 0 < x < N - 1:
                    cores.append((y, x))

    res = float("inf")
    backtrack(cores, len(cores), 0, 0)
    print(f"#{tc} {res}")

"""
1
7    
0 0 1 0 0 0 0
0 0 1 0 0 0 0
0 0 0 0 0 1 0
0 0 0 0 0 0 0
1 1 0 1 0 0 0
0 1 0 0 0 0 0
0 0 0 0 0 0 0
"""
