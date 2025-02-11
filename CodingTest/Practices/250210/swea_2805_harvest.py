T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    farm = [[*map(int, input())] for _ in range(N)]
    tot = 0
    for i in range(N):
        if i > N // 2:
            col = N - i - 1
        else:
            col = i
        for j in range(N):
            if j < N // 2:
                if j < N // 2 - col:
                    continue
            if j > N // 2:
                if j >= N - (N // 2 - col):
                    continue
            # print(i, j, farm[i][j])
            tot += farm[i][j]
    print(f"#{tc} {tot}")
