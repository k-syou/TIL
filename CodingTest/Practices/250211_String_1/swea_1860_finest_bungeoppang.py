# 1860. 진기의 최고급 붕어빵


def simulate(N, M, K, customer):
    time = 0
    bbang = 0
    idx = 0
    while idx < N:
        if time <= customer[idx]:
            time = customer[idx]
        bbang = time // M * K - idx
        while idx < N and time == customer[idx]:
            if not bbang:
                return "Impossible"
            else:
                bbang -= 1
                idx += 1
    return "Possible"


for tc in range(1, int(input()) + 1):
    N, M, K = map(int, input().split())
    customer = sorted(map(int, input().split()))
    print(f"#{tc} {simulate(N, M, K, customer)}")

"""
1
2 2 2
3 4
"""
