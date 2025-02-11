def select_sort(arr, N):
    for i in range(N - 1):
        min_idx = i
        for j in range(i + 1, N):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
