# T = int(input())
# for tc in range(1, T + 1):
#     N, K = map(int, input().split())
#     arr = [*map(int, input().split())]
#     res = 0
#     for i in range(1 << N):
#         tot = sum([n for j, n in enumerate(arr) if (i>>j) & 1])
#         if tot == K:
#             res += 1
#     print(f"#{tc} {res}")

def dfs(i, tot):
    global res
    if tot >= K:
        if tot == K:
            res += 1
        return
    if i == N:
        return
    dfs(i + 1, tot)
    dfs(i + 1, tot + arr[i])
    

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = sorted(map(int, input().split()))
    res = 0
    dfs(0, 0)
    print(f"#{tc} {res}")