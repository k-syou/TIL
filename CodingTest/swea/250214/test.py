# <출력>
# 최대한 많은 Core에 전원을 연결했을 때 전선 길이의 값의 최소값
#   - 최대한 많은 Core에 전원을 연결해도, 전원이 연결되지 않는 Core가 존재할 수 있다.

# <구현>
# 1. 코어별 모든 연결 확인하기
# 2. 연결하기
# 3. 연결끊기

# <자료구조>
# 1. 스택
# 2. 재귀

# <알고리즘>
# 1. 백트래킹
# 2. dp

import sys

sys.stdin = open("sample_input.txt", "r")

# 방향좌표
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def connected(r, c, d, length):
    """
    코어가 특정방향으로 전선을 뻗었을 때
    연결이 가능한지 여부

    연결이 가능하다면 proccesor에 전선(2) 체크

    :param r: 검사할 r 좌표
    :param c: 검사할 c 좌표
    :param d: 검사 방향
    :param length: 총 연결길이
    :return: 연결이 가능한 경우 총 연결길이, 불가능 한 경우 0
    """
    global processor, N
    nr = r + dr[d]
    nc = c + dc[d]
    # 범위를 벗어난 경우 즉 연결 완료
    if nr < 0 or nc < 0 or nr >= N or nc >= N:
        processor[r][c] = 2  # 전선 연결
        return length

    # 코어랑 만나거나, 다른 전선이 이미 있는 경우
    if processor[nr][nc] > 0:
        return 0

    # 다음 좌표 확인
    result = connected(nr, nc, d, length + 1)

    # 만약에 연결이 가능한 경우
    if result > 0:
        processor[r][c] = 2

    return result


def unconnected(r, c, d):
    """
    연결된 전선을 끊는다.
    즉 processor의 값을 0으로 변환

    :param r: 검사할 r 좌표
    :param c: 검사할 c 좌표
    :param d: 검사 방향
    """
    global processor, N
    # 선 초기화
    processor[r][c] = 0
    # 다음 좌표
    nr = r + dr[d]
    nc = c + dc[d]
    # 범위 초과
    if nr < 0 or nc < 0 or nr >= N or nc >= N:
        return
    unconnected(nr, nc, d)


def backtrack(core_idx, length, connected_count):
    """
    연결된 코어 개수별 연결 길이의 모든 경우를 찾고,
    그 중에서 최소값을 dp에 업데이트

    :param core_idx: 코어의 번호
    :param length: 연결된 전선의 길이
    :param connected_count: 연결된 코어의 개수
    """
    global processor, C, cores, dp

    # 최소값 갱신
    dp[connected_count] = min(dp[connected_count], length)

    # 모든 코어를 다 확인한 경우
    if core_idx == C:
        return

    # 4방향 연결 가능한지 검사
    # 현재 검사할 코어의 좌표
    cr, cc = cores[core_idx]
    for i in range(4):
        # 다음 방향의 좌표
        nr = cr + dr[i]
        nc = cc + dc[i]
        # 다음방향이 바로 코어가 아닌 경우에
        if processor[nr][nc] == 0:
            # 연결 여부를 파악
            connect_length = connected(nr, nc, i, 1)
            if connect_length > 0:
                # 연결이 된 경우
                backtrack(core_idx + 1, length + connect_length, connected_count + 1)
                unconnected(nr, nc, i)

    # 현재코어를 연결하지 않고 다음 코어 검사
    backtrack(core_idx + 1, length, connected_count)


T = int(input())
MAX = float("inf")
for tc in range(1, T + 1):
    N = int(input())  # 가로 세로 길이
    # 프로세서 연결 상태
    processor = [[*map(int, input().split())] for _ in range(N)]

    # 코어의 좌표 및 연결할 코어 개수 추출
    C = 0  # 코어 개수
    cores = []  # 코어들의 좌표

    # 벽에 붙지 않은 코어의 개수 및 좌표 추출
    for r in range(1, N - 1):
        for c in range(1, N - 1):
            if processor[r][c] == 1:  # 코어인 경우
                cores.append((r, c))
                C += 1

    # 연결된 코어 개수별 최소값을 담을 dp
    # 코어가 0 ~ C 개있을때의 각각의 전선의 최소값
    dp = [MAX] * (C + 1)

    # 모든 코어 연결해보기
    # 백트래킹
    backtrack(0, 0, 0)

    result = 0  # 최단 전선 길이
    for i in range(C, -1, -1):
        if dp[i] != MAX:
            result = dp[i]
            break
        else:
            dp[i] = -1

    # 출력
    print(f"#{tc}", *dp)
