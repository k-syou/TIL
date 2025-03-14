dy = [1, 0, -1, 0]
dx = [0, -1, 0, 1]


def shooting(shoot_count, weight, height, grid):
    from copy import deepcopy

    # 남은 벽돌의 개수의 최소값
    min_block_count = weight * height + 1

    def delete_block(grid, y, x, boom_range):
        '''
        벽돌 삭제하기
        '''
        # 현재 위치 0으로 만들기
        grid[y][x] = 0
        for r in range(1, boom_range):
            # 현재 위치의 벽돌 개수만큼 삭제하기
            for i in range(4):
                # 다음 위치 좌표 찾기
                ny = y + dy[i] * r
                nx = x + dx[i] * r
                # 범위 초과시 continue
                if ny < 0 or nx < 0 or ny >= height or nx >= weight:
                    continue
                # 이미 파괴된 위치인 경우
                if grid[ny][nx] == 0:
                    continue
                # 개수가 한개인 경우
                if grid[ny][nx] == 1:
                    grid[ny][nx] = 0
                    continue
                # 다음위치에서 범위 삭제 로직 재수행
                delete_block(grid, ny, nx, grid[ny][nx])

    def drop_block(grid):
        '''
        벽돌 떨어뜨리기
        '''
        for x in range(weight):
            # 행->열 순회
            
            # 가장 아래쪽에서 부터 쌓기 위함
            temp_col = [0] * height
            temp_idx = 0
            for y in range(height - 1, -1, -1):
                if grid[y][x]:
                    # 0이 아닌경우 temp_col에 쌓아둠
                    temp_col[temp_idx] = grid[y][x]
                    temp_idx += 1

            for i, y in enumerate(range(height - 1, -1, -1)):
                # 맨 블럭들 아래로 이동
                grid[y][x] = temp_col[i]

    def count_blocks(grid):
        '''
        남아있는 블록 개수 세기
        '''
        b_count = 0
        for row in grid:
            for cell in row:
                if cell:
                    b_count += 1
        return b_count

    def dfs(grid, shooting_count):
        nonlocal min_block_count
        if min_block_count == 0:
            return
        min_block_count = min(min_block_count, count_blocks(grid))
        
        # 남아있는 슈팅 기회가 없는 경우 return
        if shooting_count == 0:
            return

        for x in range(weight):
            for y in range(height):
                # 행열 순회
                if grid[y][x]:
                    # 현재 블럭 상황 복사
                    temp_grid = deepcopy(grid)
                    
                    # 삭제할 cell 비우기
                    if temp_grid[y][x] == 1:
                        # 범위가 1인 경우 0으로 만듬
                        temp_grid[y][x] = 0
                    else:
                        # 여러개인 경우 삭제후 드랍
                        delete_block(temp_grid, y, x, temp_grid[y][x])
                        drop_block(temp_grid)
                    # 다음 위치 검색
                    dfs(temp_grid, shooting_count - 1)
                    break

    # 실행
    dfs(grid, shoot_count)
    return min_block_count


T = int(input())
for tc in range(1, T + 1):
    N, W, H = map(int, input().split())
    grid = [[*map(int, input().split())] for _ in range(H)]
    print(f"#{tc} {shooting(N, W, H, grid)}")
