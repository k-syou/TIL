def recursion(arr, i, N, v):
    if i >= N:
        return 0
    if arr[i] == v:
        return 1
    return recursion(arr, i + 1, N, v)


print(recursion([1, 2, 3, 4], 0, 4, 3))
