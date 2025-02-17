from itertools import permutations
import sys

input = sys.stdin.readline
N = int(input())

innings = [[*map(int, input().split())] for _ in range(N)]
res = 0


def simulate(innings, orders):
    batting_idx = 0
    score = 0
    for inning in innings:
        outs = 0
        b1 = b2 = b3 = 0
        while outs < 3:
            result = inning[orders[batting_idx]]
            if result == 0:
                outs += 1
            elif result == 1:
                score += b3
                b1, b2, b3 = 1, b1, b2
            elif result == 2:
                score += b2 + b3
                b1, b2, b3 = 0, 1, b1
            elif result == 3:
                score += b1 + b2 + b3
                b1, b2, b3 = 0, 0, 1
            else:
                score += b1 + b2 + b3 + 1
                b1 = b2 = b3 = 0
            batting_idx = (batting_idx + 1) % 9
    return score


for pm in permutations(range(1, 9), 8):
    orders = list(pm[:3]) + [0] + list(pm[3:])
    score = simulate(innings, orders)
    if score > res:
        res = score

print(res)
