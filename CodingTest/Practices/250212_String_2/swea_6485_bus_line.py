# 6485. 삼성시의 버스 노선
for tc in range(1, int(input()) + 1):
    N = int(input())
    # 버스 노선
    bus_line = [[*map(int, input().split())] for _ in range(N)]
    P = int(input())
    # 버스 정류장 번호 리스트
    bus_stop_num = [int(input()) for _ in range(P)]
    # 버스 정류장에 서는 버스의 개수 카운팅을 위한 딕셔너리
    bus_stop = {num: 0 for num in bus_stop_num}

    for a, b in bus_line:
        # 버스 노선 시작점(a), 종료점(b)를 순회

        # 1번 방법
        ## 버스가 가는 모든 정류장을 체크하면서 카운팅
        # for i in range(a, b + 1): # a <= i <= b 를 만족하는 정수 i를 순회
        #     if i in bus_stop_num: # 해당 번호(i)의 정류장이 있는 경우
        #         bus_stop[i] += 1 # 정류장에 서는 버스 개수 횟수 + 1

        # 2번 방법
        ## 버스 정류장을 순회하며 해당 정류장이 버스가 가는 범위 안에 있는지 확인하며 카운팅
        for (
            stop
        ) in (
            bus_stop
        ):  # 버스 정류장 번호를 순회(동일한 정류장 번호가 들어올 수 있기에 key값으로 순회)
            if a <= stop <= b:  # 현재 버스정류장이 현재 노선에 들어있는지 확인
                bus_stop[stop] += 1  # 정류장에 서는 버스 개수 횟수 + 1

    # 정류장 번호가 들어온 순서대로 출력
    print(f"#{tc}", *map(lambda x: bus_stop[x], bus_stop_num))
