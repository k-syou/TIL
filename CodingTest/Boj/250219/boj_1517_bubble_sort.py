class SegmentTree:
    def __init__(self, n):
        size = 1
        while size < n:
            size *= 2
        self.tree = [0] * (size * 2)
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
                # l이 오른쪽 자식 노드에 있는 경우
                res += self.tree[l]
                l += 1
            if r % 2 == 0:
                # r이 왼쪽 자식 노드에 있는 경우
                res += self.tree[r]
                r -= 1
            # 부모 노드로 이동
            l //= 2
            r //= 2
        return res


n = int(input())
arr = [*map(int, input().split())]
nums = sorted(set(arr))
m = len(nums)
segment_tree = SegmentTree(m)
num_dict = {v: i for i, v in enumerate(nums)}
res = 0

for i in range(n):
    num = arr[i]
    pos = num_dict[num]
    res += segment_tree.query(pos + 1, m - 1)
    segment_tree.update(pos, 1)

print(res)
