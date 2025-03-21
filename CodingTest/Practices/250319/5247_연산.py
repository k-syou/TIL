from collections import deque
def bfs(n, m):
    q = deque()
    q.append((0, n))
    size = max(m, n) * 2 + 1
    visited = [0] * size
    visited[n] = 1
    while q:
        cnt, num = q.popleft()
        if num == m:
            return cnt
        for o in [1, -1, -10, 2]:
            n_num = num + o if o != 2 else num * o
            if n_num < 0 or n_num >= size:
                continue
            if visited[n_num]:
                continue
            visited[n_num] = 1
            q.append((cnt + 1, n_num))

T = int(input()) + 1
for tc in range(1, T):
    N, M = map(int, input().split())
    print(f"#{tc} {bfs(N, M)}")