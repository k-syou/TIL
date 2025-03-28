import heapq

INF = float('inf')


def dijkstra(adj, start, n):
    dist = [INF] * (n + 1)
    hq = [(0, start)]
    while hq:
        d, cur = heapq.heappop(hq)
        if d >= dist[cur]:
            continue
        dist[cur] = d
        for cost, nxt in adj[cur]:
            nd = d + cost
            if nd < dist[nxt]:
                heapq.heappush(hq, (nd, nxt))
    return dist


T = int(input().strip())
for tc in range(1, T + 1):
    N, M, X = map(int, input().split())
    # 그래프 구성 (1-indexed)
    adj = [[] for _ in range(N + 1)]
    # 역방향 그래프 구성
    radj = [[] for _ in range(N + 1)]
    for _ in range(M):
        u, v, c = map(int, input().split())
        adj[u].append((c, v))
        radj[v].append((c, u))
    # X번 집에서 출발하여 각 집까지의 최단 거리를 구함 (출발: X)
    d1 = dijkstra(adj, X, N)
    # 역방향 그래프에서 X번 집에서 출발하면, 각 집에서 X까지의 최단 거리가 됨.
    d2 = dijkstra(radj, X, N)
    
    result = 0
    for i in range(1, N + 1):
        # X번 집은 제외
        if i == X:
            continue
        result = max(result, d1[i] + d2[i])
    print(f"#{tc} {result}")

'''
어려웠던 점

기존 코드에서는 X -> 각지점 까지의 거리를 구하고,
각지점에서 X 까지의 거리를 구했다.

X -> 각지점 : O(m log n)
각지점 -> X : O(n * (m log n))
이 되서 시간초과가 났다.

역방향으로 계산을 하면
X -> 각지점         : O(m log n)
X -> 각지점(역방향) : O(m log n)
이므로 시간초과를 벗어날 수 있었다.

해당 문제에서 모든 집들간의 이동이 가능하므로 역방향으로 계산하는 발상이 가능했다.
돌아오는 문제에서 역방향을 떠올리는 발상이 중요한 것 같다.
'''