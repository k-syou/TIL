import heapq

INF = float('inf')
T = int(input()) + 1


def dijkstra1(heap):
    global dist
    while heap:
        d, cur = heapq.heappop(heap)
        if dist[cur] != INF:
            continue
        dist[cur] = d
        for nxt_d, nxt in adj[cur]:
            if dist[nxt] != INF:
                continue
            heapq.heappush(heap, (d + nxt_d, nxt))
    

def dijkstra2(heap):
    global result
    while heap:
        d, cur = heapq.heappop(heap)
        if cur == X:
            return d
        for nxt_d, nxt in adj[cur]:
            heapq.heappush(heap, (d + nxt_d, nxt))
    return 0


for tc in range(1, T):
    N, M, X = map(int, input().split())
    dist = [INF] * (N + 1)
    adj = [[] for _ in range(N + 1)]
    for _ in range(M):
        x, y, c = map(int, input().split())
        adj[x].append((c, y))
    
    heap = [(0, X)]
    dijkstra1(heap)
    result = 0
    for i in range(1, N + 1):
        if i == X:
            continue
        heap = [(dist[i], i)]
        result = max(result, dijkstra2(heap))
    
    print(f"#{tc} {result}")
