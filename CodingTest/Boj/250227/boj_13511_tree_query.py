# 이진 상승, 최소 공통 조상, RMQ, 세그먼트 트리
import sys


def dfs(i, t, d):
    global graph, dist, parent, euler, depth, first_occurrence
    # graph : 간선 그래프
    # dist : 최정상 부모 노드(1)로 부터 현재 노드(i) 까지의 가중치의 합을 나타내는 리스트
    # parent : 각 노드의 부모 노드
    # euler : 각 정점을 검색하는 순서를 표기한 리스트
    # depth : 각 정점이 검색하는 트리의 깊이를 표기한 리스트
    # first_occurrence : 각 정점이 처음 방문하는 idx 를 표기한 리스트

    if first_occurrence[i] == -1:
        first_occurrence[i] = len(depth)  # 처음 등장하는 노드의 순서

    # 검색 순서 삽입(처음 들어온 경우)
    depth.append(d)  # 깊이
    euler.append(i)  # 노드 번호

    # 탐색
    for n, w in graph[i]:
        if dist[n] != -1:  # 가중치 값이 입력된 경우 continue
            continue
        parent[n] = i  # 부모 노드 설정
        dist[n] = t + w  # 가중치 값 설정
        dfs(n, t + w, d + 1)  # 재귀

        # 검색 순서 삽입(되돌아 온 경우)
        depth.append(d)
        euler.append(i)


def min_seg_tree(depth, euler):
    # 최소값 세그먼트 트리 생성
    n = len(depth)
    size = 1
    while size < n:
        size *= 2
    seg = [(float("inf"), float("inf"))] * (size * 2)

    # 가장 하단의 트리 값 설정
    for i in range(n):
        seg[size + i] = (depth[i], euler[i])  # 깊이값, 노드 번호

    # 트리 채우기
    for i in range(size - 1, 0, -1):
        min_idx = -1
        if seg[i * 2][0] <= seg[i * 2 + 1][0]:
            min_idx = i * 2
        else:
            min_idx = i * 2 + 1

        seg[i] = seg[min_idx]

    return seg, size


def RMQ(seg, size, u, v):
    global first_occurrence
    res = (float("inf"), float("inf"))
    l = first_occurrence[u] + size
    r = first_occurrence[v] + size
    l, r = min(l, r), max(l, r)
    while l <= r:
        if l % 2 == 1:
            if seg[l][0] <= res[0]:
                res = seg[l]
            l += 1
        if r % 2 == 0:
            if seg[r][0] <= res[0]:
                res = seg[r]
            r -= 1
        l //= 2
        r //= 2
    return res[1]


def binary_lifting(N, parent):
    import math

    LOG = math.ceil(math.log2(N)) + 1

    up = [[-1] * (N + 1) for _ in range(LOG)]

    for v in range(1, N + 1):
        up[0][v] = parent[v]

    for i in range(1, LOG):
        for v in range(1, N + 1):
            if up[i - 1][v] != -1:
                up[i][v] = up[i - 1][up[i - 1][v]]

    return up


def query2(up, u, k):
    i = 0
    while k:
        if k & 1:
            u = up[i][u]
            if u == -1:
                return -1
        k //= 2
        i += 1
    return u


input = sys.stdin.readline
sys.setrecursionlimit(10**7)
N = int(input())
dist = [-1] * (N + 1)
dist[1] = 0
parent = [-1] * (N + 1)
graph = {i + 1: [] for i in range(N)}
euler = []
depth = []
first_occurrence = [-1] * (N + 1)

for _ in range(N - 1):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

dfs(1, 0, 0)
seg, size = min_seg_tree(depth, euler)
up = binary_lifting(N, parent)
M = int(input())
res = []
for _ in range(M):
    q = list(map(int, input().split()))
    u, v = q[1], q[2]
    root = RMQ(seg, size, u, v)
    if q[0] == 1:
        res.append(dist[u] + dist[v] - 2 * dist[root])
    else:
        fu, fv = first_occurrence[u], first_occurrence[v]
        fr = first_occurrence[root]
        k = q[3]
        L = (depth[fu] - depth[fr]) + (depth[fv] - depth[fr]) + 1
        if k <= (depth[fu] - depth[fr]) + 1:
            x = query2(up, u, k - 1)
        else:
            x = query2(up, v, L - k)
        res.append(x)

print(*res, sep="\n")

"""
17
1 2 0
2 3 0
3 4 0
4 5 0
5 6 0
6 7 0
7 8 0
8 9 0
1 10 0
10 11 0
11 12 0
12 13 0
13 14 0
14 15 0
15 16 0
16 17 0
6
2 9 17 1
2 9 17 2
2 9 17 3
2 9 17 4
2 9 17 12
2 9 17 17
"""
