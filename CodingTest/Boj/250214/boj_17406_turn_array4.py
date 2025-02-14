dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]


def min_row_sum(matrix):
    # 행의 합의 최소값을 구하는 함수
    return min([sum(row) for row in matrix])


def solution(A, rcs_op):
    from copy import deepcopy

    matrix = deepcopy(A)

    def turn_arr(current_value, curr_loc, se_loc, depth, end_depth):
        # 행렬 돌리기
        nonlocal matrix
        if depth == end_depth:  # 한 바뀌 다 돌았는지 확인
            return
        y, x, d = curr_loc
        next_value = matrix[y][x]
        matrix[y][x] = current_value

        sy, sx, ey, ex = se_loc  # 돌리는 기준
        ny = y + dy[d]
        nx = x + dx[d]
        nd = d
        if not (sy <= ny <= ey and sx <= nx <= ex):  # 범위를 벗어난 경우
            # 방향 전환 후 다음 좌표 재설정
            nd = (nd + 1) % 4
            ny = y + dy[nd]
            nx = x + dx[nd]
        turn_arr(next_value, (ny, nx, nd), se_loc, depth + 1, end_depth)

    for r, c, s in rcs_op:  # 입력 받은 rcs 순서대로 배열 돌리기 실행
        for i in range(2, s + 2):
            # 시작 범위 및 종료 범위 설정
            sy, sx = r - i, c - i
            ey, ex = r + i - 2, c + i - 2

            # 미리 첫 값을 빼 둔 후, 다음 좌표에 등록하면서 시작
            start_value = matrix[sy][sx]

            # 범위 좌표
            se_loc = sy, sx, ey, ex

            # 처음 들어갈 좌표 + 방향(0: 오른쪽)
            curr_loc = sy, sx + 1, 0

            # 배열이 돌아가는 길이
            t = (i * 2) - 1
            end_depth = t * t - (t - 2) ** 2

            # 배열 돌리기 실행
            turn_arr(start_value, curr_loc, se_loc, 0, end_depth)

    return min_row_sum(matrix)


from itertools import permutations

N, M, K = map(int, input().split())
A = [[*map(int, input().split())] for _ in range(N)]
rcs_op = [[*map(int, input().split())] for _ in range(K)]
res = float("inf")

for p_rcs_op in permutations(rcs_op, K):  # 모든 순서 순열 / 완전 탐색
    res = min(res, solution(A, p_rcs_op))

print(res)
