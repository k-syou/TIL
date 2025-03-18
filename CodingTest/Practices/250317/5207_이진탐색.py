def binary_search(arr, target):
    l = 0
    r = N - 1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] > target:
            r = mid - 1
        elif arr[mid] < target:
            l = mid + 1
        else:
            return True
    return False

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    A = [*map(int, input().split())]
    B = [*map(int, input().split())]
    result = 0
    for b in B:
        if binary_search(A, b):
            result += 1
    print(f"#{tc} {result}")

# print(((-1) ** .5) ** 2 + 2)