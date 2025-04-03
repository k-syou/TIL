"""
<문제요약>
유저의 수 N과 친구관계가 주어질때, a와 b의 친구 단계는 연결된 친구관계의 단계수다.
케빈 베이컨의 수는 i와 1~N(i가 아닌)인 사람들의 모든 친구 관계의 단계수를 더한 합 이다.
1 ~ N 까지의 모든 사람의 케빈 베이컨 수가 가장 작은 사람을 출력하시오.
단, 케빈 베이컨 수가 작은 사람이 여러명인 경우 번호가 낮은 사람을 출력

<입력>
N, M = 유저의 수, 친구 관계의 수
Ai, Bi = Ai 와 Bi 는 친구이다.

<알고리즘>
BFS

<문제풀이>
각 정점에서 다른 정점으로 갈 때의 거리를 모두 합한 값이 케빈 베이컨 수와 같으므로,
BFS를 활용하여 최단거리로 다른 정점에 도착할 수 있는 경우의 단계수의 합을 구하고,
비교하여 케빈 베이컨수가 가장 작은 사람을 찾아냄

1. 양방향 인접행렬 생성
2. BFS 구현
3. 한 정점에서 처음 접근하는 정점까지의 거리를 더하고, 방문처리
4. 모든 정점으로 부터의 케빈 베이컨수 확인
5. 비교하여 현재 까지 나온 케빈 베이컨 수보다 작은 경우에만 업데이트
6. 출력
"""

import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())
# 1. 양방향 인접행렬 생성
adj = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

# 2. BFS 구현
def kevin_bacon(adj, start):
    q = deque()
    q.append((0, start))
    visited = [0] * (N + 1)
    visited[start] = 1
    res = 0
    while q:
        # 3. 한 정점에서 처음 접근하는 정점까지의 거리를 더하고, 방문처리
        d, cur = q.popleft()  # d = 거리, cur = 현재 방문한 정점
        res += d  # 거리 누적
        for nxt in adj[cur]:
            if visited[nxt]:
                continue
            visited[nxt] = 1  # 방문 처리
            q.append((d + 1, nxt))
    return res

res = 0
min_v = float('inf')
for i in range(1, N + 1):
    # 4. 모든 정점으로 부터의 케빈 베이컨수 확인
    cnt = kevin_bacon(adj, i)
    # 5. 비교하여 현재 까지 나온 케빈 베이컨 수보다 작은 경우에만 업데이트
    if cnt < min_v:
        min_v = cnt
        res = i
# 6. 출력
print(res)