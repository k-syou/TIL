def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(x, y, parent, rank, size):
    rx = find(parent, x)
    ry = find(parent, y)
    if rx == ry:
        # 루트(부모)가 같은 경우
        # 사이즈 변동없이 return
        return size[rx]

    # rank가 큰쪽으로 합침
    if rank[rx] < rank[ry]:
        rx, ry = ry, rx

    # 랭크가 작은쪽에 부모 설정
    parent[ry] = rx

    # 랭크가 큰쪽에 작은쪽 사이즈만큼 사이즈 증가
    size[rx] += size[ry]

    # 둘이 랭크가 같다면 rx 쪽 랭크를 높임
    if rank[rx] == rank[ry]:
        rank[rx] += 1
    return size[rx]


def add(s):
    global i, freinds, parent, rank, size
    if s not in freinds:
        freinds[s] = i
        # 자기번호 index값으로 초기화
        parent.append(i)
        # default 값으로 초기화
        rank.append(0)
        size.append(1)
        # 인덱스 증가
        i += 1


import sys

input = sys.stdin.readline
T = int(input())

res = []
for _ in range(T):
    n = int(input())
    # 이름 인덱스화 시킬 dict
    freinds = {}

    # 유니온 파인드를 위한 배열
    parent = []
    rank = []
    size = []

    # 인덱스 번호
    i = 0
    for _ in range(n):
        # 두명의 이름을 받아옴
        a, b = input().split()
        # 유니온 파인드를 위한 초기화 작업
        add(a)
        add(b)
        # 결과값 추출
        res.append(union(freinds[a], freinds[b], parent, rank, size))
print(*res, sep="\n")
