class Shark:
    dy = [0, -1, 1, 0]
    dx = [-1, 0, 0, 1]

    def __init__(self, speed, d, size):
        self.speed = speed
        self.d = d % 4
        self.size = size

    def turn(self):
        if self.d == 0:
            return 3
        elif self.d == 1:
            return 2
        elif self.d == 2:
            return 1
        elif self.d == 3:
            return 0

    def get_next_loc(self, y, x):
        ny = y + self.dy[self.d]
        nx = x + self.dx[self.d]
        return ny, nx

    def move(self, y, x, R, C):
        ty, tx = y, x
        for _ in range(self.speed):
            ny, nx = self.get_next_loc(ty, tx)
            if ny < 0 or nx < 0 or ny >= R or nx >= C:
                self.d = self.turn()
                ny, nx = self.get_next_loc(ty, tx)
            ty, tx = ny, nx
        return ty, tx

    def __str__(self):
        return "[shark]"

    @staticmethod
    def eating(sharks):
        return max(sharks, key=lambda shark: shark.size)


R, C, M = map(int, input().split())
sea = [[None for _ in range(C)] for _ in range(R)]
shark_loc = set()
for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    sea[r - 1][c - 1] = Shark(s, d, z)
    shark_loc |= {(r - 1, c - 1)}
res = 0

for i in range(C):
    # 낚시 실행
    for j in range(R):
        if sea[j][i]:
            shark = sea[j][i]
            res += shark.size
            shark_loc -= {(j, i)}
            sea[j][i] = None
            break

    # 상어 이동
    tmp_loc = set()
    tmp_sea = [[[] for _ in range(C)] for _ in range(R)]
    for y, x in shark_loc:
        shark = sea[y][x]
        ny, nx = shark.move(y, x, R, C)
        tmp_sea[ny][nx].append(shark)
        sea[y][x] = None
        tmp_loc |= {(ny, nx)}

    # 겹치는 상어 확인
    for y, x in tmp_loc:
        if len(tmp_sea[y][x]) > 1:
            shark = Shark.eating(tmp_sea[y][x])
            tmp_sea[y][x] = [shark]
        sea[y][x] = tmp_sea[y][x][0]
    shark_loc = tmp_loc

print(res)
