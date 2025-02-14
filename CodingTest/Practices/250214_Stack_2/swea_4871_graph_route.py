# 4871. [파이썬 S/W 문제해결 기본] 4일차 - 그래프 경로 D2
def dfs(graph, i, g):
    # i = 검색 위치, g = 도착지
    if i == g:  # 현재 검색 위치가 도착지인 경우
        return 1
    for x in graph[i]:
        if dfs(graph, x, g):  # 도착한 경우 return 1
            return 1
        # 도착하지 못한 경우 다음 간선 검색
    return 0


for tc in range(1, int(input()) + 1):
    V, E = map(int, input().split())
    # 간선 그래프 정보 dict 생성
    graph = {i + 1: [] for i in range(V)}
    for _ in range(E):
        # v1 -> v2 로 갈수있는 간선 추가
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)
    S, G = map(int, input().split())
    print(f"#{tc} {dfs(graph, S, G)}")


"""
1
6 5
1 4
1 3
2 3
2 5
4 6
1 6
"""
