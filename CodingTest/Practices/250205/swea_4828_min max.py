T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [*map(int, input().split())]

    min_v = 1000001
    max_v = 0

    for num in arr:
        if min_v > num:
            min_v = num
        if max_v < num:
            max_v = num
    
    print(f'#{tc} {max_v - min_v}')