arr = [*range(4)]
N = len(arr)
for i in range(1, 1 << N):
    for j in range(N):
        if (i >> j) & 1:
            print(arr[j], end=" ")
    print()
