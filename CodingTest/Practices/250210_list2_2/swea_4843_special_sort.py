T = int(input())


def select_sort(arr, N):
    for i in range(N - 1):
        min_idx = i
        for j in range(i + 1, N):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[min_idx], arr[i] = arr[i], arr[min_idx]
    return arr


for tc in range(1, T + 1):
    N = int(input())
    arr = [*map(int, input().split())]
    arr = select_sort(arr, N)
    result = []
    for i in range(5):
        result.append(arr[-i - 1])
        result.append(arr[i])
    print(f"#{tc}", *result)
