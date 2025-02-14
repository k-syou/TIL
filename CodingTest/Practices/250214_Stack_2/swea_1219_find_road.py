# 1219. [S/W 문제해결 기본] 4일차 - 길찾기
from collections import defaultdict


def dfs(i, g):
    # 현재 노드(i)가 g에 도착한 경우
    if i == g:
        return 1

    # 현재 노드에서 갈수 있는 다음 노드 검색
    for j in graph[i]:
        if dfs(j, g):  # j번 노드에서 부터 g에 도착한 경우 return 1
            return 1
        # 도착하지 않은 경우 다음 노드 검색

    # i번 노드부터 모든 노드를 검색해도 도착하지 못한 경우
    return 0


for _ in range(10):
    tc, N = map(int, input().split())
    lines = [*map(int, input().split())]
    # defaultdict(x) : key 가 없는 경우 불러올때 기본적으로 x를 할당
    # 중복으로 들어올 수도 있기에 set 으로 설정
    graph = defaultdict(set)
    for i in range(0, N * 2, 2):
        # lines[i] => lines[i + 1] 간선 생성
        graph[lines[i]] |= {lines[i + 1]}
    print(f"#{tc} {dfs(0, 99)}")
