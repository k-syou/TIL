def shell_sort(arr):
    n = len(arr)
    gap = n // 2  # 초기 gap을 리스트 길이의 절반으로 설정

    # gap이 0이 될 때까지 반복
    while gap > 0:
        # gap 간격을 두고 삽입 정렬 수행
        for i in range(gap, n):
            temp = arr[i]
            j = i
            # 현재 원소(arr[i])보다 gap만큼 앞에 있는 원소가 크면 자리 이동
            while j >= gap and arr[j - gap] > temp:
                print(j, j-gap)
                arr[j] = arr[j - gap]
                j -= gap
            print(j)
            arr[j] = temp
        gap //= 2  # gap을 절반으로 줄임
        print(gap, arr)

    return arr

if __name__ == '__main__':
    # arr = [1, 9, 5, 2, 3, 6, 4, 8, 7, 0]
    arr = [10, 8, 6, 20, 4, 3, 22, 1, 0, 15, 16]
    print(arr)
    sorted_data = shell_sort(arr)
    print(sorted_data)