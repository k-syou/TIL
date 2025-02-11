T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    matrix = [input().split() for _ in range(N)]
    result = []
    for i in range(N):
        temp = ["", "", ""]
        for j in range(N - 1, -1, -1):
            temp[0] += matrix[j][i]
        for j in range(N - 1, -1, -1):
            temp[1] += matrix[N - i - 1][j]
        for j in range(N):
            temp[2] += matrix[j][N - i - 1]
        result.append(temp)

    print(f"#{tc}")
    for res in result:
        print(*res)
