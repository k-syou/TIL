def pascal_triangle(n):
    pascal = [[] for _ in range(n)]
    pascal[0].append(1)

    def set_pascal(n):
        nonlocal pascal
        for i in range(n + 1):
            num = 0
            if i - 1 >= 0:
                num += pascal[n - 1][i - 1]
            if n - 1 >= i:
                num += pascal[n - 1][i]
            pascal[n].append(num)

    for i in range(1, n):
        set_pascal(i)

    return pascal


for tc in range(1, int(input()) + 1):
    N = int(input())
    print(f"#{tc}")
    for row in pascal_triangle(N):
        print(*row)
