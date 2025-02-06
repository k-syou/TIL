T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [*map(int, input().split())]
    arr.sort()
    result = []
    for i in range(5):
        result.append(arr[-(i+1)])
        if N % 2 and i == N // 2 - 1:
            continue
        result.append(arr[i])

    print(f"#{tc}", *result)

