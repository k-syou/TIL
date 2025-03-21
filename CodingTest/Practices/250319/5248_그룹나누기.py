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

T = int(input()) + 1
for tc in range(1, T):
    N, M = map(int, input().split())
    data = [*map(int, input().split())]
    parent = [*range(N + 1)]
    for i in range(0, M*2, 2):
        union(data[i], data[i+1])
    
    group = set()
    for i in range(1, N+1):
        ri = find(i)
        if ri not in group:
            group.add(ri)
    
    print(f"#{tc} {len(group)}")