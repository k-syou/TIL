dy = [1, 0, -1, 0]
dx = [0, -1, 0, 1]


def shooting(shoot_count, weight, height, grid):
    from copy import deepcopy

    min_block_count = weight * height + 1

    def delete_block(grid, y, x, boom_range):
        grid[y][x] = 0
        for r in range(1, boom_range):
            for i in range(4):
                ny = y + dy[i] * r
                nx = x + dx[i] * r
                if ny < 0 or nx < 0 or ny >= height or nx >= weight:
                    continue
                if grid[ny][nx] == 0:
                    continue
                if grid[ny][nx] == 1:
                    grid[ny][nx] = 0
                    continue
                delete_block(grid, ny, nx, grid[ny][nx])

    def drop_block(grid):
        for x in range(weight):
            temp_col = [0] * height
            temp_idx = 0
            for y in range(height - 1, -1, -1):
                if grid[y][x]:
                    temp_col[temp_idx] = grid[y][x]
                    temp_idx += 1

            for i, y in enumerate(range(height - 1, -1, -1)):
                grid[y][x] = temp_col[i]

    def count_blocks(grid):
        b_count = 0
        for row in grid:
            for cell in row:
                if cell:
                    b_count += 1
        return b_count

    def dfs(grid, shooting_count):
        nonlocal min_block_count
        if shooting_count == 0:
            min_block_count = min(min_block_count, count_blocks(grid))
            return

        for x in range(weight):
            for y in range(height):
                if grid[y][x]:
                    temp_grid = deepcopy(grid)
                    if temp_grid[y][x] == 1:
                        temp_grid[y][x] = 0
                    else:
                        delete_block(temp_grid, y, x, temp_grid[y][x])
                        drop_block(temp_grid)
                    dfs(temp_grid, shooting_count - 1)
                    min_block_count = min(min_block_count, count_blocks(temp_grid))
                    break

    dfs(grid, shoot_count)
    return min_block_count


T = int(input())
for tc in range(1, T + 1):
    N, W, H = map(int, input().split())
    grid = [[*map(int, input().split())] for _ in range(H)]
    print(f"#{tc} {shooting(N, W, H, grid)}")
