def backtrack(i, tot):
    global res
    if res <= tot:
        return
    if i == N:
        res = min(res, tot)
        return
    
    for j in range(N):
        if visited[j]:
            continue
        visited[j] = 1
        backtrack(i + 1, tot + price[i][j])
        visited[j] = 0

T = int(input()) + 1

for tc in range(1, T):
    N = int(input())
    price = [[*map(int, input().split())] for _ in range(N)]
    visited = [0] * N
    res = float('inf')
    backtrack(0, 0)
    print(f"#{tc} {res}")