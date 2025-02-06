# 5 <= N <= 50
T = int(input())


def bubble_sort(arr, n):
    for i in range(n - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


for tc in range(1, T + 1):
    N = int(input())
    numbers = [*map(int, input().split())]
    numbers = bubble_sort(numbers, N)

    print(f'#{tc}', *numbers)
