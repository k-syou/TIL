T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    blue_paper = [[*map(int, input().split())] for _ in range(N)]
    red_paper = []
    i = 0
    while i < len(blue_paper):
        if blue_paper[i][4] == 1:
            red_paper.append(blue_paper.pop(i))
        else:
            i += 1

    fill_map = [[0] * 10 for _ in range(10)]

    for red in red_paper:
        for y in range(red[0], red[2] + 1):
            for x in range(red[1], red[3] + 1):
                fill_map[y][x] = 1

    for blue in blue_paper:
        for y in range(blue[0], blue[2] + 1):
            for x in range(blue[1], blue[3] + 1):
                if fill_map[y][x] == 1:
                    fill_map[y][x] = 3

    result = 0
    for col in fill_map:
        for row in col:
            if row >= 3:
                result += 1

    print(f'#{tc} {result}')