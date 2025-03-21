import heapq
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
parent = [*range(N + 1)]
rank = [0] * (N + 1)

adj = {i:{} for i in range(1, N + 1)}
for _ in range(M):
    a, b, w = map(int, input().split())
    if b not in adj[a]:
        adj[a][b] = w
    else:
        adj[a][b] = min(adj[a][b], w)
    if a not in adj[b]:
        adj[b][a] = w
    else:
        adj[b][a] = min(adj[b][a], w)


def find(a):
    pa = parent[a]
    if pa != a:
        parent[a] = find(pa)
    return parent[a]


def union(a, b):
    ra = find(a)
    rb = find(b)
    if ra != rb:
        if rank[ra] < rank[rb]:
            ra, rb = rb, ra
        rank[ra] = rank[rb] + 1
        parent[rb] = ra
        return True
    return False


def prim(adj):
    hq = []
    weight = 0
    visited = [0] * (N + 1)
    for nv in adj[1]:
        heapq.heappush(hq, (adj[1][nv], 1, nv))
    while hq:
        w, v1, v2 = heapq.heappop(hq)
        visited[v1] = 1
        if union(v1, v2):
            weight += w
            for nv in adj[v2]:
                if visited[nv]:
                    continue
                heapq.heappush(hq, (adj[v2][nv], v2, nv))
    return weight


print(prim(adj))