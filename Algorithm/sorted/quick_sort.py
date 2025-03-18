def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = []
    right = []
    for n in arr[1:]:
        if n <= pivot:
            left.append(n)
        else:
            right.append(n)
    return quick_sort(left) + [pivot] + quick_sort(right)


def quick_sort(arr, l, r):
    if l >= r:
        return
    pivot = arr[l]
    i = l + 1
    j = r
    
    while i <= j:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] >= pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[j], arr[l] = arr[l], arr[j]
    quick_sort(arr, l, j - 1)
    quick_sort(arr, j + 1, r)


# 예제 실행
if __name__ == "__main__":
    arr = [5, 2, 9, 1, 7, 6, 8, 3, 11, 3, 3, 50]
    # sorted_arr = quick_sort(arr)
    quick_sort(arr, 0, len(arr) - 1)
    print("정렬 후:", arr)
