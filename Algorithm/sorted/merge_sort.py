def merge_sort(arr):
    if len(arr) <= 1:
        return arr  # 원소가 하나면 그대로 반환

    # 1 배열을 반으로 나누기
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])  # 왼쪽 부분 정렬
    right_half = merge_sort(arr[mid:])  # 오른쪽 부분 정렬

    # 2️ 정렬된 배열 병합
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    i = j = 0  # 두 개의 배열을 비교할 포인터

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:  # 안정 정렬(같은 값이면 왼쪽 먼저)
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # 남은 요소 추가
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

# 예제 실행
if __name__ == '__main__':
    arr = [5, 2, 9, 1, 7, 6, 8, 3]
    sorted_arr = merge_sort(arr)
    print("정렬 후:", sorted_arr)