T = int(input())

# 우 하 좌 상
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

for tc in range(1, T + 1):
    N = int(input())
    snail_matrix = [[-1] * N for _ in range(N)]
    command = 0
    move = [(0, 0, 1)]

    while move:
        y, x, value = move.pop()
        snail_matrix[y][x] = value
        if value == N * N:
            break

        ny = y + dy[command]
        nx = x + dx[command]
        if 0 <= ny < N and 0 <= nx < N and snail_matrix[ny][nx] == -1:
            move.append((ny, nx, value + 1))
        else:
            command = (command + 1) % 4
            ny = y + dy[command]
            nx = x + dx[command]
            move.append((ny, nx, value + 1))

    print(f'#{tc}')
    for snail_arr in snail_matrix:
        print(*snail_arr)