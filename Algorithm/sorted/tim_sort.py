def insertion_sort(arr, left, right):
    """삽입 정렬: 작은 배열을 정렬하는 데 사용"""
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def merge(arr, left, mid, right):
    """병합 정렬의 병합 단계"""
    len1, len2 = mid - left + 1, right - mid
    left_part, right_part = arr[left:mid + 1], arr[mid + 1:right + 1]
    
    i = j = 0
    k = left
    
    while i < len1 and j < len2:
        if left_part[i] <= right_part[j]:
            arr[k] = left_part[i]
            i += 1
        else:
            arr[k] = right_part[j]
            j += 1
        k += 1

    while i < len1:
        arr[k] = left_part[i]
        i += 1
        k += 1

    while j < len2:
        arr[k] = right_part[j]
        j += 1
        k += 1

def tim_sort(arr):
    """Timsort 메인 함수"""
    n = len(arr)
    RUN = 32  # 일반적으로 Python에서 RUN 크기는 32 또는 64 사용

    # Step 1: RUN 크기만큼 나누어 삽입 정렬 수행
    for i in range(0, n, RUN):
        insertion_sort(arr, i, min(i + RUN - 1, n - 1))

    # Step 2: 병합 정렬 수행 (점점 큰 크기로 병합)
    size = RUN
    while size < n:
        for left in range(0, n, 2 * size):
            mid = left + size - 1
            right = min(left + 2 * size - 1, n - 1)

            if mid < right:
                merge(arr, left, mid, right)

        size *= 2  # 병합 크기 2배 증가

# 예제 실행
if __name__ == '__main__':
    arr = [5, 21, 7, 23, 19, 2, 32, 3, 45, 27, 8, 22]
    print("정렬 전:", arr)
    tim_sort(arr)
    print("정렬 후:", arr)