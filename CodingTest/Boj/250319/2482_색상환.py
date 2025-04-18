N = int(input())
K = int(input())
MOD = 1000000003
# dp[i][j] = i개의 색상 중에서 j개의 색을 선택한 조합의 개수(선형일 때)
dp = [[0] * (K + 1) for _ in range(N + 1)]

# 0개의 색상중 0개의 색을 선택한 경우 개수 1개
dp[0][0] = 1
# 0개의 색상중 0개의 색을 선택한 경우 개수 1개
dp[1][0] = 1
# 1개의 색상중 1개의 색을 선택한 경우 개수 1개
dp[1][1] = 1

for i in range(2, N+1):
    # i개의 색상에서 0개의 색을 선택한 경우 1개
    dp[i][0] = 1
    # (i + 1) // 2 개의 색상만 선택할 수 있다
    for j in range(1, K + 1):
        # dp[i-1][j] = i-1개의 색에 j개의 색상을 선택하는 경우(즉, i번 색상을 선택 안하는 경우)
        # dp[i-2][j-1] = i-2개의 색에 j-1개의 색상을 선택하는 경우(즉, i번 색상을 선택하는 경우)
        dp[i][j] = (dp[i-1][j] + dp[i-2][j-1]) % MOD
'''
원형이므로 추가적인 계산이 들어간다.
"1번색상을 선택하지 않은 경우의 수" + "1번 색상을 선택한 경우의 수"

1. 1번 색상을 선택하지 않은경우
  2~N 범위 색상들을 K개 뽑은 경우의 수
  즉 N-1개의 색상들을 K개 뽑은 경우의 수와 같다.

2. 1번 색상을 선택한 경우
  2번과 N번 색상을 선택하지 못하므로,
  3~N-1 범위의 색상들을 K-1개 뽑은 경우의 수
  즉 N-3개의 색상들을 K-1개 뽑은 경우의 수와 같다.
'''
res = (dp[N-1][K] + dp[N-3][K-1]) % MOD
print(res)