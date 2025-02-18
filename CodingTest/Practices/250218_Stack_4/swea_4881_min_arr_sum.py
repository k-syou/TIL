def backtrack(matrix, visited, i, tot):
    global res
    if res < tot:
        return
    if i == N:
        res = min(res, tot)
        return
    for x in range(N):
        if visited[x]:
            continue
        visited[x] = True
        backtrack(matrix, visited, i + 1, tot + matrix[i][x])
        visited[x] = False


for tc in range(1, int(input()) + 1):
    N = int(input())
    visited = [False] * N
    matrix = [[*map(int, input().split())] for _ in range(N)]
    res = 10**9
    backtrack(matrix, visited, 0, 0)
    print(f"#{tc} {res}")
