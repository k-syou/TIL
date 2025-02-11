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
            dp[i] = max(dp[i], dp[i - calorie] + taste)

    print(f"#{tc} {max(dp)}")
