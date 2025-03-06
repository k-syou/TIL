def f(N, city):
    result = 0
    for i in range(2, N - 2):
        max_height = 0
        # for j in range(i - 2, i + 3):
        #     if i != j and max_height < city[j]:
        #         max_height = city[j]
        max_height = max(city[i - 2], city[i - 1], city[i + 1], city[i + 2])
        views = city[i] - max_height
        if views > 0:
            result += views
    return views


T = 10
for tc in range(1, T + 1):
    N = int(input())
    city = list(map(int, input().split()))
    result = f(N, city)
    print(f"#{tc} {result}")
