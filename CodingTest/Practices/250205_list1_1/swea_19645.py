T = int(input())


def binary_search(page, target):
    l, r, c = 1, page, (page + 1) // 2
    count = 1
    while True:
        if c == target:
            return count
        count += 1
        if c < target:
            l = c
        else:
            r = c
        c = (l + r) // 2


for tc in range(1, T + 1):
    P, A, B = map(int, input().split())
    res_a = binary_search(P, A)
    res_b = binary_search(P, B)
    if res_a == res_b:
        res = 0
    elif res_a > res_b:
        res = 'B'
    else:
        res = 'A'

    print(f'#{tc} {res}')
