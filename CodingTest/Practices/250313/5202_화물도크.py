def get_max_work(i, cnt):
    '''
    완전 탐색(조합)
    '''
    global result
    result = max(result, cnt)
    for j in range(i + 1, N + 1):
        if work_time[i][1] <= work_time[j][0]:
            get_max_work(j, cnt + 1)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())  # 신청서 개수
    # 시작시간 - 종료시간 배열
    work_time = [[0, 0]] + sorted([[*map(int, input().split())] for _ in range(N)])
    result = 0
    get_max_work(0, 0)
    print(f"#{tc} {result}")
