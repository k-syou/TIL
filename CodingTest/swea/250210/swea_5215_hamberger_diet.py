T = int(input())

for tc in range(1, T + 1):
    N, L = map(int, input().split())
    taste_calorie = [[*map(int, input().split())] for _ in range(N)]
    result = 0
    dp = [0] * (L + 1)
    # dp 원리
    # 순회하며 칼로리별 맛의 최대값을 저장
    for taste, calorie in taste_calorie:
        for i in range(L, calorie - 1, -1):
            # 현재 칼로리(i)의 위치에
            # 저장된 칼로리 dp[i]와 해당 햄버거를 먹은 경우 dp[i - calorie]에 taste를 더한 합 중
            # 더 큰 값을 갱신
            dp[i] = max(dp[i], dp[i - calorie] + taste)
        # print(taste, calorie, dp)
    print(f"#{tc} {max(dp)}")

"""
1
5 10
1 2
3 5
2 3
5 10
4 4
"""
