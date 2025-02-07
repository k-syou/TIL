def magic_square_LUX(N):
    half = N // 2
    magic_odd = magic_square_odd(half)  # 홀수 마방진 (3×3, 5×5 등)

    # 4개의 블록 생성
    A = [[magic_odd[i][j] for j in range(half)] for i in range(half)]
    B = [[magic_odd[i][j] + 2 * (half ** 2) for j in range(half)] for i in range(half)]
    C = [[magic_odd[i][j] + 3 * (half ** 2) for j in range(half)] for i in range(half)]
    D = [[magic_odd[i][j] + (half ** 2) for j in range(half)] for i in range(half)]

    # L 패턴 (첫 번째 열 일부 교환)
    swap_count = half // 2
    for i in range(swap_count):
        A[i][0], C[i][0] = C[i][0], A[i][0]

    # U 패턴 (중앙 열 일부 교환)
    for i in range(swap_count + 1, half):
        B[i][0], D[i][0] = D[i][0], B[i][0]

    # 중앙 X 패턴 조정 (N이 6, 10, 14 등일 때 일반적인 규칙 적용)
    if half >= 4:  # N = 10, 14, 18 ... 등의 경우에도 적용
        A[swap_count][1], C[swap_count][1] = C[swap_count][1], A[swap_count][1]

    # 최종적으로 N×N 배열에 배치
    magic_square = [[0] * N for _ in range(N)]
    for i in range(half):
        for j in range(half):
            magic_square[i][j] = A[i][j]  # 왼쪽 위
            magic_square[i][j + half] = B[i][j]  # 오른쪽 위
            magic_square[i + half][j] = C[i][j]  # 왼쪽 아래
            magic_square[i + half][j + half] = D[i][j]  # 오른쪽 아래

    return magic_square


# 홀수 마방진 함수
def magic_square_odd(N):
    magic_square = [[0] * N for _ in range(N)]
    y, x = 0, N // 2  # 첫 번째 행의 중앙부터 시작
    for num in range(1, N * N + 1):
        magic_square[y][x] = num
        ny, nx = (y - 1) % N, (x + 1) % N
        if magic_square[ny][nx]:  # 이미 숫자가 있으면 아래로 이동
            y = (y + 1) % N
        else:
            y, x = ny, nx
    return magic_square


# 짝수 마방진 함수
def magic_square_even_4n(N):
    magic_square = [[(i * N + j + 1) for j in range(N)] for i in range(N)]

    # 대각선 패턴을 뒤집기
    for i in range(N):
        for j in range(N):
            if (i % 4 == j % 4) or ((i % 4 + j % 4) == 3):
                magic_square[i][j] = N * N + 1 - magic_square[i][j]

    return magic_square


N = int(input())
if N % 2:  # 홀수 마방진
    square = magic_square_odd(N)
elif N % 4 == 0:  # 4의 배수일 때
    square = magic_square_even_4n(N)
else:  # 4의 배수가 아닌 짝수 (6, 10, 14, ...)
    square = magic_square_LUX(N)

for row in square:
    print(*row)
