# 1767. [SW Test 샘플문제] 프로세서 연결하기
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


def connected(y, x, d, cnt):
    # 코어의 연결 여부와 연결 전선의 길이(line)를 return
    # 또한 방문기록도 남김(1: 전선)
    global processor
    if processor[y][x]:
        return 0
    ny = y + dy[d]
    nx = x + dx[d]
    if ny < 0 or nx < 0 or ny >= N or nx >= N:
        # 연결된 경우(범위 밖으로 나간경우)
        processor[y][x] = 1
        return cnt
    line = connected(ny, nx, d, cnt + 1)
    if line:
        processor[y][x] = 1
    else:
        processor[y][x] = 0
    return line


def unconnected(y, x, d):
    # 연결된 전선(1)을 processor에서 0으로 변경
    global processor
    processor[y][x] = 0
    ny = y + dy[d]
    nx = x + dx[d]
    if ny < 0 or nx < 0 or ny >= N or nx >= N:
        return
    unconnected(ny, nx, d)


def backtrack(cores, C, i, lines, connect_count):
    # cores = 각 코어의 좌표, C = 코어의 개수, i = 검색할 코어의 번호
    # lines : 총 전선 연결 길이, connect_count = 코어 연결 개수
    global min_lines
    # 현재 코어의 연결 개수(connect_count)의 전선 연결 길이(lines)를
    # 이전에 할당된 값과 비교하여 최소값 입력
    min_lines[connect_count] = min(min_lines[connect_count], lines)
    if i == C:  # 마지막 코어까지 검색한 경우 종료
        return
    y, x = cores[i]
    for d in range(4):  # 4방향 검색
        ny = y + dy[d]
        nx = x + dx[d]
        if ny < 0 or nx < 0 or ny >= N or nx >= N:
            # 범위 초과인 경우 다음방향 검색
            continue
        lines_cnt = connected(ny, nx, d, 1)  # 연결 가능한지 확인
        if lines_cnt:  # 연결이 가능한 경우
            # 연결 개수를 1늘리고 연결된 전선의 개수를 누적하여 다음 코어 검색
            backtrack(cores, C, i + 1, lines + lines_cnt, connect_count + 1)
            # 다음 방향 검색을 위한 연결 해제
            unconnected(ny, nx, d)
    # 연결이 되지 않아도 다음 코어를 검색 해야함
    backtrack(cores, C, i + 1, lines, connect_count)


for tc in range(1, int(input()) + 1):
    N = int(input())
    processor = [[*map(int, input().split())] for _ in range(N)]
    cores = []

    # 검색할 코어의 위치 검색
    for y in range(N):
        for x in range(N):
            if processor[y][x] == 1:
                processor[y][x] = 3  # 코어의 위치(테스트할 때 보기위함)
                if 0 < y < N - 1 and 0 < x < N - 1:
                    # 벽에 붙어있지 않은 코어의 위치만 검색하면 되므로 범위를 지정하여 추가
                    cores.append((y, x))

    # 전체 코어가 연결이 되지 않아도 수행해야 하고 최대로 많이 연결된 경우에
    # 최소값을 찾아야 하기 때문에 코어가 연결된 개수 별 전선 길이의 최소값 배열(min_lines)를 생성
    min_lines = [float("inf")] * (len(cores) + 1)

    # 백트래킹 실행
    backtrack(cores, len(cores), 0, 0, 0)

    # 코어가 최대로 많이 연결된 경우의 최소 전선 개수 할당(res)
    for i in range(len(cores), -1, -1):
        if min_lines[i] != float("inf"):
            res = min_lines[i]
            break
    print(f"#{tc} {res}")


# test
# N = 7
# processor = [
#     [0, 0, 1, 0, 0, 0, 0],
#     [0, 0, 1, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 1, 0],
#     [0, 0, 0, 0, 0, 0, 0],
#     [1, 1, 0, 1, 0, 0, 0],
#     [0, 1, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0],
# ]
# visited = [[0] * N for _ in range(N)]
# cores = []
# for y in range(N):
#     for x in range(N):
#         if processor[y][x] == 1:
#             visited[y][x] = 3
#             if 0 < y < N - 1 and 0 < x < N - 1:
#                 cores.append((y, x))
# print(cores[0])
# for i in range(4):
#     y, x = cores[0]
#     ny = y + dy[i]
#     nx = x + dx[i]
#     cnt = connected(ny, nx, i, 1)
#     print(cnt)
#     for row in visited:
#         print(*row)
#     unconnected(ny, nx, i)
"""
1
7    
0 0 1 0 0 0 0
0 0 1 0 0 0 0
0 0 0 0 0 1 0
0 0 0 0 0 0 0
1 1 0 1 0 0 0
0 1 0 0 0 0 0
0 0 0 0 0 0 0
"""
