def get_dist(y1, x1, y2, x2):
    return abs(y1 - y2) + abs(x1 - x2)


def backtrack(y, x, visited, depth, dist):
    global res
    if res <= dist:
        return

    if depth == n:
        dist += get_dist(y, x, gy, gx)
        res = min(res, dist)
        return

    for i in range(n):
        if visited[i]:
            continue
        ny, nx = loc[i]
        tmp_dist = get_dist(y, x, ny, nx)
        visited[i] = True
        backtrack(ny, nx, visited, depth + 1, dist + tmp_dist)
        visited[i] = False


for tc in range(1, int(input()) + 1):
    n = int(input())
    sy, sx, gy, gx, *arr = [*map(int, input().split())]
    loc = []
    res = float("inf")
    for i in range(0, n * 2, 2):
        loc.append((arr[i], arr[i + 1]))
    visited = [False] * n
    backtrack(sy, sx, visited, 0, 0)
    print(f"#{tc} {res}")
