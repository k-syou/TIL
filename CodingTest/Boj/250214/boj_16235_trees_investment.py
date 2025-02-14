# 16235, 나무 재테크
# from pprint import pprint
from collections import deque

dy = [-1, -1, -1, 0, 1, 1, 1, 0]
dx = [-1, 0, 1, 1, 1, 0, -1, -1]


def spring():
    global trees, nourishment
    # 자신의 나이 만큼 양분을 먹고 나이가 1 증가
    # 여러 나무가 있는 경우 어린 나무 부터 양분을 먹는다.
    # 양분이 부족하다면 양분을 먹지 않고 죽는다.
    death_trees = []
    for y in range(N):
        for x in range(N):
            for j in range(len(trees[y][x])):
                if nourishment[y][x] >= trees[y][x][j]:
                    nourishment[y][x] -= trees[y][x][j]
                    trees[y][x][j] += 1
                else:
                    # 양분이 부족한 경우 해당 나무보다 큰 경우에는 전부다 제거
                    while (len(trees[y][x]) - 1) >= j:
                        v = trees[y][x].pop()
                        death_trees.append((y, x, v))
                    break
    return death_trees


def summer(death_trees):
    global nourishment
    # 죽은 나무의 나이를 2로 나눈 몫을 양분으로 추가
    for y, x, v in death_trees:
        nourishment[y][x] += v // 2


def fall():
    global trees
    # 현재의 trees의 나이가 5의 배수인 경우
    # 주변 8방향에 나이가 1인 나무를 추가
    add_trees = 0
    for y in range(N):
        for x in range(N):
            for _ in [j for j in trees[y][x] if j % 5 == 0]:
                for i in range(8):
                    ny = y + dy[i]
                    nx = x + dx[i]
                    if ny < 0 or nx < 0 or ny >= N or nx >= N:
                        continue
                    trees[ny][nx].appendleft(1)
                    add_trees += 1
    return add_trees


def winter():
    global nourishment
    # 로봇 S2D2가 돌아다니며 A 만큼의 양분을 추가한다.
    for y in range(N):
        for x in range(N):
            nourishment[y][x] += A[y][x]


N, M, K = map(int, input().split())
# 나무의 나이가 담긴 행렬
trees = [[deque() for _ in range(N)] for _ in range(N)]
# 양분 행렬
nourishment = [[5] * N for _ in range(N)]
A = [[*map(int, input().split())] for _ in range(N)]

# 기존에 심은 나무 추가 및 초기 나무 개수
tree_cnt = M
init_tree_loc = set()
for _ in range(M):
    r, c, age = map(int, input().split())
    init_tree_loc |= {(r - 1, c - 1)}
    trees[r - 1][c - 1].append(age)

# 나무 크기 정렬(오름차순)
for y, x in init_tree_loc:
    trees[y][x] = deque(sorted(trees[y][x]))

# print("\n초기 양분")
# pprint(nourishment)

# print("\n초기 나무")
# pprint(trees)

# K년 동안 사이클 진행
for year in range(K):
    death_trees = spring()  # 죽은 나무 return
    tree_cnt -= len(death_trees)  # 죽은 나무만큼 나무 개수 감소
    summer(death_trees)  # 죽은 나무 양분 추가
    tree_cnt += fall()  # 추가된 나무 개수만큼 나무 개수 추가
    winter()  # S2D2 로봇이 양분 추가
    # print(f"\n{year + 1}년 후 양분")
    # pprint(nourishment)

    # print(f"\n{year + 1}년 후 나무")
    # pprint(trees)

print(tree_cnt)
