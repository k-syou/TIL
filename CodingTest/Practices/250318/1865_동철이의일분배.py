import sys
sys.stdin = open("input.txt", "r")
res_out = []

def backtrack(r, tot):
    global res
    if tot <= res:
        # 이미 결과보다 낮은경우 나머지가 최선의 경우인
        # 100%(1)을 곱해도 똑같음
        return
    if r == N:
        # 결과 갱신
        res = max(res, tot)
        return
    for c in range(N):
        if visited[c]:
            continue
        visited[c] = 1
        backtrack(r + 1, tot * work[r][c])
        visited[c] = 0


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    # 일을 퍼센트 단위로 받아옴
    work = [[*map(lambda x: int(x) / 100, input().split())] for _ in range(N)]
    visited = [0] * N
    res = 0
    backtrack(0, 1)
    # print(f"#{tc} {format(round(res * 100, 7), '.6f')}")
    # 문제에서 반올림 하라고 되어있는데 반올림 하면 틀림(버림 해야함)
    res_out.append(f"#{tc} {format(round(res * 100, 6), '.6f')}")
    # print(f"#{tc} {format(round(res * 100, 6), '.6f')}")

output = open("output.txt", "r")
x = output.readlines()
for i, s in enumerate(x):
    if s.strip() != res_out[i]:
        print(s.strip(), res_out[i])