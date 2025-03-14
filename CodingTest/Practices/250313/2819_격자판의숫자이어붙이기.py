def backtrack(y, x, s, depth):
    global sets
    if depth == 7:
        sets.add(s)
        return
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if ny < 0 or nx < 0 or ny >= N or nx >= N:
            continue
        backtrack(ny, nx, s + board[ny][nx], depth + 1)

T = int(input())
dy = (-1, 0, 1, 0)
dx = (0, 1, 0, -1)

for tc in range(1, T + 1):
    N = 4
    board = [input().split() for _ in range(N)]
    sets = set()
    for y in range(N):
        for x in range(N):
            backtrack(y, x, board[y][x], 1)
    print(f"#{tc} {len(sets)}")
