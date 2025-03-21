import heapq

# INF = float('inf')


def prim(adj, s):
    global N
    hq = [(0, s)]
    visited = [0] * (N + 1)
    dist = 0
    cnt = 0
    while hq:
        w, node = heapq.heappop(hq)
        if visited[node]:
            continue
        visited[node] = 1
        dist += w
        cnt += 1
        if cnt == N + 1:
            break

        for n_node, n_w in adj[node]:
            if not visited[n_node]:
                heapq.heappush(hq, (n_w, n_node))

    return dist


def find(a):
    pa = parent[a]
    if a != pa:
        parent[a] = find(pa)
    return parent[a]


def union(a, b):
    ra = find(a)
    rb = find(b)
    if ra != rb:
        parent[rb] = ra
        return True
    return False


T = int(input()) + 1
for tc in range(1, T):
    N, E = map(int, input().split())
    hq = []
    parent = [*range(N + 1)]
    adj = [[] for _ in range(N + 1)]
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        adj[n1].append((n2, w))
        adj[n2].append((n1, w))
        heapq.heappush(hq, (w, n1, n2))

    cnt = 0
    result = 0
    while hq and cnt < N:
        w, n1, n2 = heapq.heappop(hq)
        if union(n1, n2):
            cnt += 1
            result += w
    # print(f"#{tc} {prim(adj, 0)}")
    print(f"#{tc} {result}")
