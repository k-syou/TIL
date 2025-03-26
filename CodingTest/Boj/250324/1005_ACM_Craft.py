import sys, heapq

input = sys.stdin.readline
T = int(input())


def build(heap):
    global indegree, graph
    while heap:
        cur_time, cur_num = heapq.heappop(heap)
        if cur_num == W:
            return cur_time

        for nxt_num in graph[cur_num]:
            indegree[nxt_num] -= 1
            if indegree[nxt_num] == 0:
                heapq.heappush(heap, (cur_time + D[nxt_num], nxt_num))


res = []
for _ in range(T):
    N, K = map(int, input().strip().split())
    D = [None] + [*map(int, input().strip().split())]

    graph = [[] for _ in range(N + 1)]
    indegree = [0] * (N + 1)
    for _ in range(K):
        x, y = map(int, input().strip().split())
        graph[x].append(y)
        indegree[y] += 1
    W = int(input())
    
    heap = []
    for i in range(1, N + 1):
        if indegree[i] == 0:
            heapq.heappush(heap, (D[i], i))
    
    res.append(build(heap))

print(*res, sep="\n")