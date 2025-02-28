import sys

input = sys.stdin.readline


class Fenw:
    def __init__(self, n, arr):
        self.n = n
        self.bit1 = [0] * (n + 1)
        self.bit2 = [0] * (n + 1)
        for i in range(n):
            l, w = i + 1, arr[i]
            self.update(l, w)
            if l + 1 <= n:
                self.update(l + 1, -w)

    def update(self, l, w):
        w2 = (l - 1) * w
        while l <= self.n:
            self.bit1[l] += w
            self.bit2[l] += w2
            l += l & -l

    def query(self, x):
        s1 = s2 = 0
        while x > 0:
            s1 += self.bit1[x]
            s2 += self.bit2[x]
            x -= x & -x
        return s1, s2

    def prefix(self, i):
        s1, s2 = self.query(i)
        return s1 * i - s2


n, m, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]

fenw = Fenw(n, arr)
res = []
for _ in range(m + k):
    a, *data = map(int, input().split())
    if a == 1:
        b, c, d = data
        fenw.update(b, d)
        if c + 1 <= n:
            fenw.update(c + 1, -d)
    else:
        b, c = data
        res.append(fenw.prefix(c) - fenw.prefix(b - 1))

print(*res, sep="\n")
