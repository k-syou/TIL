T = int(input())


def kill_flies(matrix, y, x, M):
    dy = [[-1, 0, 1, 0], [-1, -1, 1, 1]]
    dx = [[0, -1, 0, 1], [-1, 1, -1, 1]]
    result = 0
    for c in range(2):
        total = matrix[y][x]
        for i in range(4):
            for m in range(1, M):
                ny = y + dy[c][i] * m
                nx = x + dx[c][i] * m
                if 0 <= ny < N and 0 <= nx < N:
                    total += matrix[ny][nx]
        result = max(result, total)
    return result


for tc in range(1, T + 1):
    N, M = map(int, input().split())
    fly_map = [[*map(int, input().split())] for _ in range(N)]
    max_v = 0
    for y in range(N):
        for x in range(N):
            max_v = max(max_v, kill_flies(fly_map, y, x, M))

    print(f'#{tc} {max_v}')