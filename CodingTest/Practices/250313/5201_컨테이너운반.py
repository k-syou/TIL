T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    weight = sorted(map(int, input().split()), reverse=True)
    visited = [0] * N
    truck = sorted(map(int, input().split()), reverse=True)
    t = 0
    tot_weight = 0
    w = 0
    while t < M:
        while w + 1 < N and truck[t] < weight[w]:
            w += 1
        while w + 1 < N and visited[w]:
            w += 1
        if visited[w]:
            break
        visited[w] = 1
        tot_weight += weight[w]
        t += 1
    print(f"#{tc} {tot_weight}")


'''
18 13 12 11 2
20 20 17 9 9 7 7 5 4 3
'''