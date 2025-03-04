def find(a, parent):
    pa = parent[a]
    if pa != a:
        parent[a] = find(pa, parent)
    return parent[a]


def merge(a, b, parent):
    # 연결
    ra = find(a, parent)
    rb = find(b, parent)
    if ra != rb:
        parent[rb] = ra


def check(a, b, parent):
    # 연결 여부 확인
    ra = find(a, parent)
    rb = find(b, parent)
    if ra == rb:
        return "YES"
    return "NO"


import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

n, m = map(int, input().split())
parent = [i for i in range(n + 1)]
res = []
for _ in range(m):
    o, a, b = map(int, input().split())
    if o == 0:
        # 0일때는 둘을 연결
        merge(a, b, parent)
    else:
        # 1일때는 연결 여부 확인
        res.append(check(a, b, parent))
print(*res, sep="\n")
