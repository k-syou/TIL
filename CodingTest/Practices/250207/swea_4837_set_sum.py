T = int(input())


def backtrack(visited, n, tot, counts):
    global result
    if counts == N:
        if tot == K:
            result += 1
        return
    if tot >= K:
        return
    for i in range(n, 13):
        if not visited[i]:
            visited[i] = True
            backtrack(visited, i + 1, tot + i, counts + 1)
            visited[i] = False


for tc in range(1, T + 1):
    N, K = map(int, input().split())
    result = 0
    visited = [False] * 13
    for i in range(1, 13 - N):
        visited[i] = True
        backtrack(visited, i + 1, i, 1)
        visited[i] = False
    print(f'#{tc} {result}')


# bit_masking
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = [*range(13)]
    result = 0
    for i in range(1 << 12):
        cnt = 0
        tot = 0
        for j in range(12):
            if i & (i << j):
                cnt += 1
                tot += arr[j]
                if cnt > N:
                    break
        if cnt == N and tot == K:
            result += 1
    print(f'#{tc} {result}')