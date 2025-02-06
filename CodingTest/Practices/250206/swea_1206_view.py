for tc in range(1, 11):
    N = int(input())
    buildings = [*map(int, input().split())]

    views = 0
    for i in range(2, N-2):
        max_v = max(buildings[i-2], buildings[i-1], buildings[i+1], buildings[i+2])
        diff = buildings[i] - max_v
        if diff > 0:
            views += diff

    print(f'#{tc} {views}')