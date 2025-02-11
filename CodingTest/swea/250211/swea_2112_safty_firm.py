def searching(firms, K):
    for x in range(W):
        max_c = 0
        for y in range(D):
            if y == 0:
                cnt = 0
                f_type = firms[y][x]
            if f_type == firms[y][x]:
                cnt += 1
            else:
                cnt = 0
                f_type = firms[y][x]
            max_c = max(max_c, cnt)
            if cnt == K:
                continue
        if max_c < K:
            return False
    return True


def solution(D, W, K, firms):
    if searching(firms, K):
        return 0

    res = K

    def dfs(i, firms, cnt):
        nonlocal res
        if cnt >= res:
            return
        for x in range(i + 1, D):
            if searching(firms, K):
                res = min(res, cnt)
            dfs(x, firms, cnt)
            tmp_firm1 = firms[:]
            tmp_firm1[x] = [0] * W
            if searching(tmp_firm1, K):
                res = min(res, cnt + 1)
            dfs(x, tmp_firm1, cnt + 1)
            tmp_firm2 = firms[:]
            tmp_firm2[x] = [1] * W
            if searching(tmp_firm1, K):
                res = min(res, cnt + 1)
            dfs(x, tmp_firm2, cnt + 1)

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
"""
