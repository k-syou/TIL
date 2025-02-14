T = int(input())
for tc in range(1, T + 1):
    K, N, M = map(int, input().split())
    bus_stop = [False] * (N + 1)
    for i in map(int, input().split()):
        bus_stop[i] = True

    start = 0
    charge_count = 0

    while True:
        tmp = start
        start += K
        if start >= N:
            break
        for i in range(start, tmp - 1, -1):
            if bus_stop[i]:
                start = i
                charge_count += 1
                break

        if start == tmp:
            charge_count = 0
            break

    print(f'#{tc} {charge_count}')