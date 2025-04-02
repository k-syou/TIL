import heapq, sys

input = sys.stdin.readline


def find(node):
    global parent
    p_node = parent[node]
    if p_node != node:
        parent[node] = find(parent[node])
    return parent[node]


def union(a, b):
    global parent
    p_a = find(a)
    p_b = find(b)
    # print(f"a, b = {a}, {b} | p_a, p_b = {p_a}, {p_b}")
    if p_a != p_b:
        parent[p_b] = p_a
        return True
    return False

N, M = map(int, input().split())
arr = [''] + input().split()

# 크루스칼
heap = []

for _ in range(M):
    a, b, w = map(int, input().split())
    heapq.heappush(heap, (w, a, b))

parent = [*range(N + 1)]
# 연결한 간선의 개수가 N - 1개가 될때까지 반복
cnt = 0
tot = 0
while heap:
    weight, a, b = heapq.heappop(heap)
    if arr[a] == arr[b]:
        continue
    if union(a, b):
        cnt += 1
        tot += weight
        if cnt == N - 1:
            break

if cnt != N - 1:
    tot = -1
print(tot)