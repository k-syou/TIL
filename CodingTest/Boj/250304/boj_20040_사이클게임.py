import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)


def find(a, parent):
    if a != parent[a]:
        parent[a] = find(parent[a], parent)
    return parent[a]


def union(a, b, parent):
    ra = find(a, parent)
    rb = find(b, parent)
    if ra != rb:
        parent[rb] = ra
        return True
    return False


def cycle_game():
    n, m = map(int, input().split())
    parent = [i for i in range(n)]
    lines = [[*map(int, input().split())] for _ in range(m)]
    res = 1
    for a, b in lines:
        if not union(a, b, parent):
            return res
        res += 1
    return 0


print(cycle_game())
