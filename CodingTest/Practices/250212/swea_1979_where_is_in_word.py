# 1979. 어디에 단어가 들어갈 수 있을까


def search(y, x, is_row):
    if is_row:
        d = [0, 1]
    else:
        d = [1, 0]
    res = 1
    ny, nx = y, x
    while ny < N and nx < N:
        ny += d[0]
        nx += d[1]
        if ny >= N or nx >= N:
            break
        if board[ny][nx] == 0:
            break
        res += 1
    return res == K


for tc in range(1, int(input()) + 1):
    N, K = map(int, input().split())
    board = [[*map(int, input().split())] for _ in range(N)]
    res = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                if (i - 1 < 0 or board[i - 1][j] == 0) and search(i, j, False):
                    res += 1
                if (j - 1 < 0 or board[i][j - 1] == 0) and search(i, j, True):
                    res += 1
    print(f"#{tc} {res}")
