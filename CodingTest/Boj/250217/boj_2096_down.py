import sys

input = sys.stdin.readline
N = int(input())
max_v = [*map(int, input().split())]
min_v = max_v[:]
for i in range(1, N):
    scores = [*map(int, input().split())]
    max_v = [
        max(max_v[:2]) + scores[0],
        max(max_v) + scores[1],
        max(max_v[1:]) + scores[2],
    ]
    min_v = [
        min(min_v[:2]) + scores[0],
        min(min_v) + scores[1],
        min(min_v[1:]) + scores[2],
    ]

print(max(max_v), min(min_v))
