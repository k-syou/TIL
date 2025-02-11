from collections import deque

T = int(input())  # 테스트 케이스


class Microorganism:
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    def __init__(self, y, x, dist, cnt, move_count=0):
        self.y = y
        self.x = x
        self.dist = dist
        self.cnt = cnt
        self.move_count = move_count
        self.merged = False

    def move(self, N):
        ny = self.y + self.dy[self.dist]
        nx = self.x + self.dx[self.dist]
        if ny == 0 or nx == 0 or ny == N - 1 or nx == N - 1:
            self.cnt //= 2
            if self.dist <= 1:
                self.dist = 0 if self.dist else 1
            else:
                self.dist = 2 if self.dist == 3 else 3
        self.y = ny
        self.x = nx
        self.move_count += 1

    def __str__(self):
        return f"({self.y}, {self.x}), cnt : {self.cnt}, move : {self.move_count}, dist : {self.dist}, merged : {self.merged}"

    @staticmethod
    def merge(micr_1, micr_2):
        micr_1.cnt += micr_2.cnt
        micr_2.merged = True


def bfs(microorganisms):
    q = deque(microorganisms)
    visited = [[[] for _ in range(N)] for _ in range(N)]
    x = 0
    res = 0

    def merge(micr_list):
        micr_list.sort(key=lambda micr: micr.cnt, reverse=True)
        main_micr = micr_list[0]
        for micr in micr_list[1:]:
            Microorganism.merge(main_micr, micr)

    while q:
        micr = q.popleft()
        if micr.move_count == M:
            continue
        if micr.move_count != x:
            for i in range(N):
                for j in range(N):
                    if len(visited[i][j]) > 1:
                        merge(visited[i][j])
                    visited[i][j] = []
            x += 1
        if micr.merged:
            continue
        micr.move(N)
        if micr.cnt == 0:
            continue
        visited[micr.y][micr.x].append(micr)
        q.append(micr)

    for micr in microorganisms:
        if not micr.merged and micr.move_count == M:
            res += micr.cnt
    return res


for tc in range(1, T + 1):
    # 구역의 크기(N*N), 격리시간, 군집 개수
    N, M, K = map(int, input().split())
    microorganisms = []
    for _ in range(K):
        ty, tx, cnt, tdist = map(int, input().split())
        microorganisms.append(Microorganism(ty, tx, tdist - 1, cnt))
    print(f"#{tc} {bfs(microorganisms)}")
