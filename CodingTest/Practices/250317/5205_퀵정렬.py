def quick_sort(p, end):
    if p >= end:
        return
    
    pivot = arr[p]
    l = p + 1
    r = end
    
    while l <= r:
        while l <= r and arr[l] <= pivot:
            l += 1
        while l <= r and arr[r] >= pivot:
            r -= 1
        if l < r:
            arr[l], arr[r] = arr[r], arr[l]
    if p < r:
        arr[p], arr[r] = arr[r], arr[p]
    
    quick_sort(p + 1, r - 1)
    quick_sort(r + 1, end)

for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = [*map(int, input().split())]
    quick_sort(0, N - 1)
    print(f"#{tc} {arr[N//2]}")
