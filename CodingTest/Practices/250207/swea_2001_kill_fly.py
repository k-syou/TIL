T = int(input())


def get_prefix_sum_matrix(matrix, n):
    result = [[0] * n for _ in range(n)]
    dy = [-1, -1, 0]
    dx = [-1, 0, -1]
    for y in range(n):
        for x in range(n):
            result[y][x] = matrix[y][x]
            for i in range(3):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0 <= ny < n and 0 <= nx < n:
                    if i == 0:
                        result[y][x] -= result[ny][nx]
                    else:
                        result[y][x] += result[ny][nx]
    return result


def prefix_sum(matrix, y, x, m):
    total = matrix[y][x]
    ny = y - m
    nx = x - m
    if ny >= 0:
        total -= matrix[ny][x]
    if nx >= 0:
        total -= matrix[y][nx]
    if ny >= 0 and nx >= 0:
        total += matrix[ny][nx]
    return total


for tc in range(1, T + 1):
    N, M = map(int, input().split())
    fly_map = [[*map(int, input().split())] for _ in range(N)]
    prefix_sum_matrix = get_prefix_sum_matrix(fly_map, N)

    max_v = 0
    for y in range(M - 1, N):
        for x in range(M - 1, N):
            max_v = max(max_v, prefix_sum(prefix_sum_matrix, y, x, M))

    print(f'#{tc} {max_v}')


# 1
# 5 2
# 1 3 3 6 7
# 8 13 9 12 8
# 4 16 11 12 6
# 2 4 1 23 2
# 9 13 4 7 3