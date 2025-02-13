def get_distance(y, x):
    # 0, 0 으로부터 거리 계산
    return abs(y) + abs(x)


def get_searching_loc(K):
    # 거리가 k 만큼 차이나는 좌표들을 searching_loc[k] 배열에 저장
    # searching_loc = [[(0, 0)], [(-1, 0), (0, -1), (0, 1), (1, 0)] ...]
    searching_loc = [[None] * ((i - 1) * 4 if i > 1 else 1) for i in range(1, K + 1)]
    index_list = [0] * (K + 1)
    for y in range(-K, K + 1):
        for x in range(-K, K + 1):
            dist = get_distance(y, x)
            if dist >= K:
                continue
            searching_loc[dist][index_list[dist]] = (y, x)
            index_list[dist] += 1

    return searching_loc


def searching(y, x, k, city, searching_loc, N, dp_v):
    # 0 ~ k-1 까지 현재 좌표에 저장된 값에
    # searching_loc[k]에 저장된 좌표 값(거리가 k인 좌표)
    # 위치에 건물(1)이 있으면 누적
    tot = dp_v
    for dy, dx in searching_loc[k]:
        ny = y + dy
        nx = x + dx
        if ny < 0 or nx < 0 or ny >= N or nx >= N:
            continue
        tot += city[ny][nx]

    # 범위 내 총 건물 수 출력
    return tot


def solustion(N, M, city):
    res = 0
    # 가운데에서 모든 칸을 채울 수 있는 경우까지 확인(N + 2)
    searching_loc = get_searching_loc(N + 2)
    # 동적 계획법
    # 칸별로 각 k(거리)별 총합을 기록
    dp = [[[0] * (N + 2) for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            dp[i][j][0] = city[i][j]

    for k in range(N + 2):
        start = (
            k // 2 - 1 if k > 1 else 0
        )  # k 범위가 커질 수록 반드시 확인 하지 않아도 되는 범위가 생김
        for y in range(start, N - start):
            for x in range(start, N - start):
                # before: dp에 저장된 y,x 좌표의 0 ~ k-1 까지의 집의 수
                if k == 0:  # 단 k == 0 인경우 저장된 값이 없기에 0
                    before = 0
                else:
                    before = dp[y][x][k - 1]
                dp[y][x][k] = searching(y, x, k, city, searching_loc, N, before)

                # 현재 수익률
                price = M * dp[y][x][k] - ((k + 1) ** 2 + k**2)
                if price >= 0:  # 손해보지 않으면 max 집 개수 설정
                    res = max(res, dp[y][x][k])
    return res


for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    city = [[*map(int, input().split())] for _ in range(N)]
    print(f"#{tc} {solustion(N, M, city)}")
