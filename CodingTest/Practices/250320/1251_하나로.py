import heapq


def find(a):
    pa = parent[a]
    if pa != a:
        parent[a] = find(pa)
    return parent[a]


def union(a, b):
    ra = find(a)
    rb = find(b)
    if ra != rb:
        parent[rb] = ra
        return True
    return False


def prim(x, y, e):
    hq = []
    for i in range(1, N):
        L = ((x[i] - x[0])**2 + (y[i] - y[0])**2) * e
        heapq.heappush(hq, (L, i))
    result = 0
    cnt = 0
    visited = [0] * N
    visited[0] = 1
    while hq and cnt < N - 1:
        dist, a = heapq.heappop(hq)
        if visited[a]:
            continue
        cnt += 1
        result += dist
        visited[a] = 1
        for i in range(N):
            if visited[i]:
                continue
            L = ((x[i] - x[a])**2 + (y[i] - y[a])**2) * e
            heapq.heappush(hq, (L, i))
    return result


T = int(input()) + 1

for tc in range(1, T):
    N = int(input())
    X = [*map(int, input().split())]
    Y = [*map(int, input().split())]
    E = float(input())
    parent = [*range(N)]
    print(f"#{tc} {prim(X, Y, E)}")
    # 크루스칼
    # hq = []
    # for i in range(N):
    #     for j in range(i + 1, N):
    #         L = ((X[i] - X[j])**2 + (Y[i] - Y[j])**2) * E
    #         heapq.heappush(hq, (L, i, j))
    # cnt = 0
    # result = 0
    # while hq and cnt < N - 1:
    #     l, a, b = heapq.heappop(hq)
    #     # print(l, a, b)
    #     if union(a, b):
    #         cnt += 1
    #         result += l
    
    # result = int(round(result))
    # print(f"#{tc} {result}")

'''
1
2
0 0
0 100
1.0
'''