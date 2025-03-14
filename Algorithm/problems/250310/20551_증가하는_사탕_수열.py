T = int(input())
for tc in range(1, T + 1):
    arr = [*map(int, input().split())]
    N = len(arr)
    result = 0
    for i in range(N - 2, -1, -1):
        if arr[i + 1] <= 1:
            result = -1
            break
        if arr[i + 1] <= arr[i]:
            diff = arr[i] - arr[i+1] + 1
            result += diff
            arr[i] -= diff
    print(f"#{tc} {result}")