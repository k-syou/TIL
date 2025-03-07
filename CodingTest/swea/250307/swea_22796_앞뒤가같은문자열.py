def cal_str_cnt(s1, s2):
    n, m = len(s1), len(s2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    # s1[:i] 와 s2[:j] 가 같아지게 하는 개수
    # s1 = 'str'
    # s2 = 'xfr'
    # dp = [
    #   [0, 1, 2, 3], : [''    -> '', ''    -> 'x', ''    -> 'xf', ''    -> 'xfr']
    #   [1, 1, 2, 3], : ['s'   -> '', 's'   -> 'x', 's'   -> 'xf', 's'   -> 'xfr']
    #   [2, 2, 2, 3], : ['st'  -> '', 'st'  -> 'x', 'st'  -> 'xf', 'st'  -> 'xfr']
    #   [3, 3, 3, 2], : ['str' -> '', 'str' -> 'x', 'str' -> 'xf', 'str' -> 'xfr']
    # ]
    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0:
                # s1 가 빈 글자인 경우
                dp[i][j] = j
            elif j == 0:
                # s2 가 빈 글자인 경우
                dp[i][j] = i
            elif s1[i - 1] != s2[j - 1]:
                # 검사중인 글자에 마지막 글자가 다른 경우
                # dp[i - 1][j] + 1: s1[:i-1] 이 s2[:j]   와 같아지는 연산 + 1
                # dp[i][j - 1] + 1: s1[:i]   이 s2[:j-1] 와 같아지는 연산 + 1
                # dp[i-1][j-1] + 1: s1[:i-1] 이 s2[:j-1] 와 같아지는 연산 + 1
                dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + 1)
            else:
                # dp[i-1][j-1] + 1: s1[:i-1] 이 s2[:j-1] 와 같아지는 연산
                dp[i][j] = dp[i - 1][j - 1]

    return dp[n][m]


T = int(input())
for _ in range(T):
    s = input()
    N = len(s)
    result = N
    if N > 1:
        for i in range(N):
            s1 = s[:i]
            s2 = s[i:]
            result = min(result, cal_str_cnt(s1, s2))
    print(result)
