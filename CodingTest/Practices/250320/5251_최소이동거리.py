import heapq

T = int(input()) +1


def dijkstra(adj):
    hq = [(0, 0)]
    while hq:
        dist, v = heapq.heappop(hq)
        if v == N:
            return dist
        for nv in adj[v]:
            heapq.heappush(hq, (dist + adj[v][nv], nv))

for tc in range(1, T):
    N, E = map(int, input().split())
    adj = {i:{} for i in range(N + 1)}
    for _ in ' '*E:
        s, e, w = map(int, input().split())
        if e not in adj[s]:
            adj[s][e] = w
        else:
            adj[s][e] = min(adj[s][e], w)
    print(f"#{tc} {dijkstra(adj)}")