def check_sdoku(sdoku):
    for i in range(9):
        a, b, c = [0] * 10, [0] * 10, [0] * 10
        for j in range(9):
            if a[sdoku[i][j]]:
                return 0
            a[sdoku[i][j]] = 1
            if b[sdoku[j][i]]:
                return 0
            b[sdoku[j][i]] = 1
            if c[sdoku[(i // 3) * 3 + (j // 3)][(j % 3) + (i % 3) * 3]]:
                return 0
            c[sdoku[(i // 3) * 3 + (j // 3)][(j % 3) + (i % 3) * 3]] = 1
    return 1


for tc in range(1, int(input()) + 1):
    print(f"#{tc} {check_sdoku([[*map(int, input().split())] for _ in range(9)])}")


"""
1
7 3 6 4 2 9 5 8 1
5 8 9 1 6 7 3 2 4
2 1 4 5 8 3 6 9 7
8 4 7 9 3 6 1 5 2
1 5 3 8 4 2 9 7 6
9 6 2 7 5 1 8 4 3
4 2 1 3 9 8 7 6 5
3 9 5 6 7 4 2 1 8
6 7 8 2 1 5 4 3 9
"""
