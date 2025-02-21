from collections import deque


def bfs(S, G, nodes):
    q = deque()
    visited = [False] * (V + 1)  # 방문기록
    q.append((S, 0))  # 시작지점 및 초기 거리
    visited[S] = True  # 시작지점 방문 체크
    while q:  # 큐에 요소 있을때만 작동
        curr_node, curr_dist = q.popleft()  # 제일 먼저들어온 노드 및 거리정보
        if curr_node == G:  # 도착한 경우
            return curr_dist  # 거리정보를 리턴
        for next_node in nodes[curr_node]:  # 갈수있는 노드 순회
            if visited[next_node]:  # 이미 방문한 경우 skip
                continue
            visited[next_node] = True  # 방문기록 남김
            q.append((next_node, curr_dist + 1))  # 다음위치와 거리를 큐에 추가
    # 갈 수 없는 경우
    return 0


for tc in range(1, int(input()) + 1):
    V, E = map(int, input().split())
    nodes = {i + 1: [] for i in range(V)}  # 간선 정보 초기화
    for _ in range(E):
        # 무방향 간선 정보 생성
        a, b = map(int, input().split())
        nodes[a].append(b)
        nodes[b].append(a)
    S, G = map(int, input().split())  # 시작노드, 도착노드
    print(f"#{tc} {bfs(S, G, nodes)}")
