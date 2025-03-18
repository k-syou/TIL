def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    global result
    if left[-1] > right[-1]:
        result += 1
    
    i = j = 0
    merge_arr = [0] * (len(left) + len(right))
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merge_arr[i + j] = left[i]
            i += 1
        else:
            merge_arr[i + j] = right[j]
            j += 1
    
    while i < len(left):
        merge_arr[i + j] = left[i]
        i += 1
    
    while j < len(right):
        merge_arr[i + j] = right[j]
        j += 1
    
    return merge_arr


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [*map(int, input().split())]
    result = 0
    sort_arr = merge_sort(arr)
    
    print(f"#{tc} {sort_arr[N // 2]} {result}")




