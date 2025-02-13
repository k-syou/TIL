def dfs(parent, i):
    global res, visited
    # 현재 정점의 값이 이미 검색(출력)된 경우
    if visited[i]:
        return

    # 부모 노드 검색
    for j in parent[i]:
        if visited[j]:
            continue
        # 부모 노드가 아직 검색(출력) 하지 않은 경우 재귀 호출
        dfs(parent, j)

    # 모든 부모 노드가 검색이 된 후 현재 노드 검색(출력)
    visited[i] = True
    res.append(i)


for tc in range(1, 11):
    V, E = map(int, input().split())
    # parent : 노드별 부모 노드의 정점들(list)을 담을 변수
    parent = {i + 1: [] for i in range(V)}
    # lines: 입력받은 간선 정보(E 개의 (부모노드, 자식노드))
    lines = [*map(int, input().split())]
    # visited: 노드가 이미 검색(출력) 되었는지 확인하는 배열
    visited = [False] * (V + 1)

    # 결과값(노드 순서)을 담을 배열
    res = []

    # 도착지(lines[i + 1])에 부모 노드(lines[i])를 추가
    for i in range(0, E * 2, 2):
        parent[lines[i + 1]].append(lines[i])

    # 낮은 정점부터 검색 시작
    for i in range(1, V + 1):
        dfs(parent, i)

    print(f"#{tc}", *res)
