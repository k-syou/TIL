for _ in range(10):
    tc = int(input())
    # 100 x 100 배열 읽기
    matrix = [[*map(int, input().split())] for _ in range(100)]
    max_v = 0

    # 행렬의 합중 최대값
    for i in range(100):
        # 비교: 현재 최대값, 행의 합, 열의 합
        max_v = max(max_v, sum(matrix[i]), sum([row[i] for row in matrix]))
    # 대각선의 합중 최대값
    # 비교: 현재 최대값, 우하향 대각선의 합, 좌하향 대각선의 합
    max_v = max(max_v, sum([matrix[i][i] for i in range(100)]), sum([matrix[i][99 - i] for i in range(100)]))

    # 출력
    print(f'#{tc} {max_v}')
