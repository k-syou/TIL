T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lines = [[*map(int, input().split())] for _ in range(N)]
    result = 0
    for i in range(N):
        for j in range(i + 1, N):
            if (
                (lines[i][0] < lines[j][0] and lines[i][1] > lines[j][1]) or 
                (lines[i][0] > lines[j][0] and lines[i][1] < lines[j][1])
                ):
                result += 1
    print(f"#{tc} {result}")