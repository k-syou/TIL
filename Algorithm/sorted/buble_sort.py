# 버블정렬
def bubble_sort(arr, N):
    for i in range(N-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

if __name__ == '__main__':
    arr = [55, 7, 78, 12, 42]
    print(arr)
    print(bubble_sort(arr, len(arr)))