def dfs(stars_dp:dict, i:int):
    if stars_dp[i]:
        return stars_dp[i]
    
    before_stars:list = dfs(stars_dp, i - 1)
    now_stars:list = before_stars[:]
    if i % 3 == 2:
        for j in range(len(now_stars)):
            now_stars[j] += ' ' * (i // 3 + 1) + '*'
    elif i % 3 == 0:
        now_stars.append('*' * len(now_stars[0]))
    else:
        now_stars.extend(before_stars)
    stars_dp[i] = now_stars
    return stars_dp[i]
        
    
stars_dp = {i:[] for i in range(1, 37)}
stars_dp[1] = ['*']


T = int(input())
for tc in range(1, T + 1):
    print(f"#{tc}")
    print(*dfs(stars_dp, int(input())), sep='\n')