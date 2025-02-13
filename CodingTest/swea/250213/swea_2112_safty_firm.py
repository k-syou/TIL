def searching(firms, K):
    # 현재 필름이 K 깊이만큼 동일한 타입으로 막이 형성되어있는지 확인(성능검사)
    ## 열 우선 순회
    for x in range(W):
        f_type = firms[0][x]
        cnt = 1
        for y in range(1, D):
            if f_type == firms[y][x]:
                cnt += 1
            else:  # 타입이 다른경우 개수와 필름 타입 초기화
                cnt = 1
                f_type = firms[y][x]
            if cnt == K:  # 조건을 만족하는 경우 break
                break
        if cnt < K:  # 하나라도 성능검사 통과 못할 경우 False 리턴
            return False
    return True  # 모든 성능검사 통과 한 경우 True 리턴


def solution(D, W, K, firms):
    # 성능검사 통과하는 최소 개수의 필름 변경 값을 리턴하는 로직

    # K == 1 인경우 어떤 경우에도 만족 함으로 0 리턴
    if K == 1:
        return 0

    # 최소값을 K로 설정
    ## K번 바꾸면 무조건 성공하기 때문
    res = K

    def dfs(i, firms, cnt):
        nonlocal res
        if searching(firms, K):  # 성능검사 통과 시 res 값 설정
            res = min(res, cnt)
        if cnt + 1 >= res:  # 현재 cnt + 1 이 저장된 최소값 보다 큰경우 종료
            # 이미 현재 필름이 성능검사가 통과 된지 알고있음
            # 실패한 경우 필름을 바꿔야만 성공이 가능한 상황이므로
            # cnt + 1이 최소값과 동일하거나 큰경우에는 검토할 필요가 없음
            return
        if i >= D:
            # 마지막 인덱스인 경우 종료
            return

        # 모든 경우를 탐색하기 위해 3가지 경우로 탐색
        # 1. 필름 변경을 하지않고 검색
        dfs(i + 1, firms, cnt)

        # 2. i 번째 필름을 0, 0, ... 으로 변경 검색
        tmp_firm1 = firms[:]
        tmp_firm1[i] = [0] * W
        dfs(i + 1, tmp_firm1, cnt + 1)

        # 3. i 번째 필름을 1, 1, ... 으로 변경 후 검색
        tmp_firm2 = firms[:]
        tmp_firm2[i] = [1] * W
        dfs(i + 1, tmp_firm2, cnt + 1)

    # 첫 행을 변경할지에서 시작하여 검색
    dfs(0, firms, 0)
    return res


for tc in range(1, int(input()) + 1):
    D, W, K = map(int, input().split())
    firms = [[*map(int, input().split())] for _ in range(D)]
    print(f"#{tc} {solution(D, W, K, firms)}")

"""
1
6 8 3
0 0 1 0 1 0 0 1
0 1 0 0 0 1 1 1
0 1 1 1 0 0 0 0
1 1 1 1 0 0 0 1
0 1 1 0 1 0 0 1
1 0 1 0 1 1 0 1

1
6 8 3
0 0 1 0 1 0 0 1
0 1 0 0 0 1 1 1
0 0 0 0 0 0 0 0
1 1 1 1 0 0 0 1
0 1 1 0 1 0 0 1
1 1 1 1 1 1 1 1
"""
