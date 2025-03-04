import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)
n = int(input())
adj = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

# dp로 검사할 색의 개수
# n개 ~ 10개(최대)
K = min(10, n)
dp = [None] * (n + 1)


def dfs(u, parent, dp):
    # 현재 노드의 dp 초기화
    dp[u] = [0] * (K + 1)

    # 색깔별 점수 기본값
    for i in range(1, K + 1):
        dp[u][i] = i

    for v in adj[u]:
        if v == parent:
            # 부모 노드인 경우 pass
            continue
        # 자식 노드인 경우
        # 자식노드의 자식 노드를 찾는다.
        dfs(v, u, dp)

        for i in range(1, K + 1):
            # i : 현재 노드의 색 번호
            best = float("inf")
            for x in range(1, K + 1):
                # x : 자식노드의 색 번호
                if x == i:
                    continue
                best = min(dp[v][x], best)
            # 현재노드를 i로 설정했을때의 최소 값을 더함
            dp[u][i] += best
    # 자식노드가 더이상 없는 경우 종료


dfs(1, -1, dp)
print(min(dp[1][1:]))
