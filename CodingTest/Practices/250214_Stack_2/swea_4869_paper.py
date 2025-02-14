# 23558. 4869. [파이썬 S/W 문제해결 기본] 4일차 - 종이붙이기

# dfs 풀이
# def dfs(x, g):
#     global res
#     if x > g:  # 현재 길이가 도착 길이를 초과 하는 경우 종료
#         return
#     if x == g:  # 현재 길이가 도착 길이와 같은 경우
#         # 최종 완성 가능 개수의 + 1
#         res += 1
#         return
#     dfs(x + 10, g)  # 20 x 10 을 붙힌경우
#     dfs(x + 20, g)  # 10 x 20 을 두장 붙힌 경우
#     dfs(x + 20, g)  # 20 x 20 을 한장 붙힌 경우


# for tc in range(1, int(input()) + 1):
#     res = 0
#     dfs(0, int(input()))
#     print(f"#{tc} {res}")

# dp 풀이
for tc in range(1, int(input()) + 1):
    goal = int(input()) // 10
    dp = [1, 1, 3] + [0] * (goal - 2)
    for i in range(3, goal + 1):
        """
        i-1 일 때 20 * 10 한개를 두는 경우의 수가 존재
        i-2 일 때 10 * 20 두개 혹은 20 * 20 을 둘수있는 두가지 경우 존재

        즉 i일때는
        (i-1 번째 나올수있는 모든 경우의 수) + (i-2 번째 나올 수 있던 모든 경우의 수의 2배)
        이며, 위계산으로 i일때의 경우의 수를 알 수 있음
        dp[0] = 1
        dp[1] = dp[0](20 * 10 한개) = 1
        dp[2] = dp[1](20 * 10 두개를 놓은 것) + dp[0] * 2(20 * 20 and 10 * 20 경우의 수 두개) = 3
        dp[3] = dp[2] + dp[1] * 2
        ...
        dp[goal] = dp[goal-1] + dp[goal-2] * 2

        """
        dp[i] = dp[i - 1] + dp[i - 2] * 2
    print(f"#{tc} {dp[goal]}")
