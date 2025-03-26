import sys, heapq
input = sys.stdin.readline
N, M = map(int, input().strip().split())

# 자신보다 늦게 풀어야할 문제가 있는지 저장할 변수
graph = [[] for _ in range(N + 1)]

# 자신보다 먼저 출력되어야 할 문제의 개수
indegree = [0] * (N+1)

for _ in range(M):
    a, b = map(int, input().strip().split())
    # 늦게 풀어야할 문제 추가
    graph[a].append(b)
    # 먼저 풀어야할 개수 증가
    indegree[b] += 1

heap = []
for i in range(1, N + 1):
    if indegree[i] == 0:
        # 먼저 풀어야할 문제가 없는 경우
        # 낮은 난이도의 문제부터 출력하도록 heap에 추가
        heapq.heappush(heap, i)

res = []
while heap:
    # 풀어야할 문제
    cur = heapq.heappop(heap)
    res.append(cur)
    # 해당 문제 다음에 풀어야할 문제가 있으면 방문 처리
    for nxt in graph[cur]:
        # 먼저 풀어야할 문제 개수 감소
        indegree[nxt] -= 1
        # 먼저 풀어야할 문제가 없다면 heap에 추가
        if indegree[nxt] == 0:
            heapq.heappush(heap, nxt)

print(*res)