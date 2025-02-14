# 17136, 색종이 붙이기
import sys

sys.setrecursionlimit(10**7)
dy = [0, 1, 1]
dx = [1, 1, 0]

N = 10
M = 5
paper = [[*map(int, input().split())] for _ in range(N)]
visited = [[0] * N for _ in range(N)]
one_cnt = 0
paper_type = [0] + [5] * 5
res = float("inf")

# 종이의 1을 누적합으로 만듬
# 1 1 1    3 2 1
# 1 1 1 => 2 2 1
# 1 1 1    1 1 1
for y in range(N - 1, -1, -1):
    for x in range(N - 1, -1, -1):
        if paper[y][x]:
            visited[y][x] = 1
            one_cnt += 1
        if y == N - 1 or x == N - 1:
            continue
        if paper[y][x]:
            paper[y][x] = min(map(lambda i: paper[y + dy[i]][x + dx[i]], range(3))) + 1
            if paper[y][x] > 5:
                paper[y][x] = 5


def gluing(y, x, m):
    # 종이 붙히기
    for i in range(m):
        for j in range(m):
            if visited[i + y][j + x] == 0:
                return False
    for i in range(m):
        for j in range(m):
            visited[i + y][j + x] = 0
    return True


def ungluing(y, x, m):
    # 종이 제거
    for i in range(m):
        for j in range(m):
            visited[i + y][j + x] = 1


def next_loc(y, x):
    # 다음 종이 붙힐 위치 찾기
    for i in range(y, N):
        for j in range(N):
            if i == y and j <= x:
                continue
            if visited[i][j] == 1 and paper[i][j] > 0:
                return i, j
    return -1, -1


def backtrack(y, x, cnt, one_cnt):
    # 붙힐수 있는 가장 큰 종이 부터 붙혀가면서 완전 탐색
    global res
    if res < cnt:
        return
    if one_cnt == 0:
        res = min(res, cnt)
        return
    if y < 0:
        return
    if paper[y][x]:
        for m in range(paper[y][x], 0, -1):
            if not paper_type[m]:  # 크기별 남은 종이 개수 확인
                continue
            if not gluing(y, x, m):  # 종이 붙히기 가능한지 확인 및 붙히기
                continue
            ny, nx = next_loc(y, x)  # 다음위치 찾기
            paper_type[m] -= 1  # 해당 크기 종이 개수 - 1
            backtrack(ny, nx, cnt + 1, one_cnt - m * m)
            # 백트래킹 후 원상 복구
            paper_type[m] += 1
            ungluing(y, x, m)
    else:  # 가릴 부분이 아닌 경우
        ny, nx = next_loc(y, x)
        backtrack(ny, nx, cnt, one_cnt)


# 백트래킹 검색 시작
backtrack(0, 0, 0, one_cnt)

# 종이가 모자란 경우
if res == float("inf"):
    res = -1

print(res)
