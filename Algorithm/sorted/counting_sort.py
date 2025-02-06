# 카운팅 정렬
# n이 비교적 작고, k가 인덱스로 표현 가능한(정수) 일때만 가능
def counting_sort(arr, N, k):
    counts_length = k + 1
    counts = [0] * counts_length
    temp = [0] * N

    for num in arr:
        counts[num] += 1

    for i in range(1, counts_length):
        counts[i] += counts[i-1]

    for i in range(N - 1, -1, -1): # 역순으로 하지않으면 비안정 정렬로 정렬됨
        counts[arr[i]] -= 1
        idx = counts[arr[i]]
        temp[idx] = arr[i]
    
    return temp

if __name__ == '__main__':
    data = [0, 4, 1, 3, 1, 2, 4, 1]
    N = 8
    k = 4
    print(data)
    print(counting_sort(data, N, k))