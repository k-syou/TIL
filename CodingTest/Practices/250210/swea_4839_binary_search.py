T = int(input())


def binary_search(L, R, target):
    center = (L + R) // 2
    left, right = L, R
    try_count = 0
    while left != right:
        if center == target:
            break
        if center > target:
            right = center
        else:
            left = center
        center = (left + right) // 2
        try_count += 1
    return try_count


for tc in range(1, T + 1):
    P, A, B = map(int, input().split())
    a_count = binary_search(1, P, A)
    b_count = binary_search(1, P, B)
    res = "0"
    if a_count > b_count:
        res = "B"
    elif a_count < b_count:
        res = "A"
    print(f"#{tc} {res}")
