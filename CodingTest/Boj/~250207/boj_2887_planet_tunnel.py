import heapq, sys
input = sys.stdin.readline
MAX = sys.maxsize

N = int(input())
x_loc, y_loc, z_loc, edges = [], [], [], []
for i in range(N):
    x, y, z = map(int, input().split())
    x_loc.append((x, i))
    y_loc.append((y, i))
    z_loc.append((z, i))
x_loc.sort()
y_loc.sort()
z_loc.sort()
for i in range(N - 1):
    w1, i1 = x_loc[i]
    w2, i2 = x_loc[i + 1]
    edges.append([abs(w1 - w2), i1, i2])
    w1, i1 = y_loc[i]
    w2, i2 = y_loc[i + 1]
    edges.append([abs(w1 - w2), i1, i2])
    w1, i1 = z_loc[i]
    w2, i2 = z_loc[i + 1]
    edges.append([abs(w1 - w2), i1, i2])
heapq.heapify(edges)


def find(parent, a):
    if parent[a] != a:
        parent[a] = find(parent, parent[a])
    return parent[a]


def union(parent, a, b, rank):
    root_a = find(parent, a)
    root_b = find(parent, b)
    if root_a != root_b:
        if rank[root_a] > rank[root_b]:
            parent[root_b] = root_a
        elif rank[root_a] < rank[root_b]:
            parent[root_a] = root_b
        else:
            parent[root_b] = root_a
            rank[root_a] += 1
        return True
    return False


parent = [*range(N)]
rank = [0] * N
mtx_weight = 0
connected_count = 0

while edges:
    w, a, b = heapq.heappop(edges)
    if union(parent, a, b, rank):
        mtx_weight += w
        connected_count += 1
        if connected_count == N - 1:
            break

print(mtx_weight)