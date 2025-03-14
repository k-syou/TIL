T = int(input())

for tc in range(1, T + 1):
    daily, month, three_month, years = map(int, input().split())
    use_days = [0] + [*map(int, input().split())]
    dp = [years] * 13
    dp[1] = min(daily * use_days[1], month, three_month)
    for i in range(2, 13):
        if i > 3:
            dp[i] = min(dp[i], dp[i-3] + three_month)
        else:
            dp[i] = min(dp[i], three_month)
        dp[i] = min(dp[i], dp[i-1] + daily * use_days[i], dp[i-1] + month)
    print(f"#{tc} {dp[12]}")


# 재귀 풀이
# def cal(m, tot):
#     global min_value
#     if m > 12:
#         min_value = min(min_value, tot)
#         return
    
#     cal(m + 1, tot + use_days[m] * daily)
#     cal(m + 1, tot + month)
#     cal(m + 3, tot + three_month)

# T = int(input())

# for tc in range(1, T + 1):
#     daily, month, three_month, years = map(int, input().split())
#     use_days = [0] + [*map(int, input().split())]
#     min_value = years
#     cal(1, 0)
#     print(f"#{tc} {min_value}")