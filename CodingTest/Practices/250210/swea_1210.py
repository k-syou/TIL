def ladder(start_point):
    dy = [0, 0, -1]  # 좌, 우, 상
    dx = [-1, 1, 0]
    move = [start_point]
    move_idx = 2
    while move:
        y, x = move.pop()
        if y == 0:
            return x
        if move_idx == 2:
            for i in range(2):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0 > ny or ny >= 100 or 0 > nx or nx >= 100:
                    continue
                if matrix[ny][nx] == 0:
                    continue
                move_idx = i
                break

        if move_idx != 2:
            ny = y + dy[move_idx]
            nx = x + dx[move_idx]
            if 0 <= ny < 100 and 0 <= nx < 100 and matrix[ny][nx]:
                move.append((ny, nx))
            else:
                move_idx = 2
                ny = y + dy[move_idx]
                nx = x + dx[move_idx]
                move.append((ny, nx))
        else:
            ny = y + dy[move_idx]
            nx = x + dx[move_idx]
            move.append((ny, nx))
    return


for _ in range(10):
    tc = int(input())
    matrix = [[*map(int, input().split())] for _ in range(100)]
    start = (99, matrix[-1].index(2))
    print(f'#{tc} {ladder(start)}')
