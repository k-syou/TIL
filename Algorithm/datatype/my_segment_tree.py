class SegmentTree:
    def __init__(self, n):
        self.n = n
        size = 1
        while size < n:
            size *= 2
        self.tree = [0] * (2 * size)
        self.size = size

    def update(self, pos, v):
        pos += self.size
        while pos:
            self.tree[pos] += v
            pos //= 2

    def query(self, l, r):
        l += self.size
        r += self.size
        res = 0
        while l <= r:
            if l % 2:
                res += self.tree[l]
                l += 1
            if r % 2 == 0:
                res += self.tree[r]
                r -= 1
            l //= 2
            r //= 2
        return res
