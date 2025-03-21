class SegmentTree:
    def __init__(self, L):
        self.size = 1
        while self.size < L:
            self.size *= 2
        self.tree = [0] * (self.size * 2 + 1)
    
    def update(self, i):
        node = self.size + i
        while node > 0:
            self.tree[node] += 1
            node //= 2
    
    def qeury(self, a):
        l = self.size
        r = self.size + a - 1
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


class Fenw:
    __slot__ = ['size', 'bit1']
    def __init__(self, N):
        self.size = N + 1
        self.bit1 = [0] * (self.size)
    
    def update(self, i, w):
        size = self.size
        bit1 = self.bit1
        while i < size:
            bit1[i] += w
            i += i & -i
            # 0110110
            # 1001010
            #     010
            
            #  (2 ^ 31 -1)
            # - 2 ^ 31
            
    
    def query(self, i):
        sum_bit1 = 0
        bit1 = self.bit1
        while i > 0:
            sum_bit1 += bit1[i]
            i -= i & -i
        return sum_bit1

# def fenw_update(i, w):
#     global tree
#     while i < size:
#         tree[i] += w
#         i += i & -i

# def fenw_query(i):
#     global tree
#     s = 0
#     while i > 0:
#         s += tree[i]
#         i -= i & -i
#     return s
import sys
from bisect import bisect_right, bisect_left
sys.stdin = open('input.txt', 'r')
data = sys.stdin.buffer.read().split()
N = int(data[0])
arr = [int(x) for x in data[1:]]
sort_arr = sorted(arr)
comp_arr = [bisect_right(sort_arr, n) for n in arr]
size = N + 1
tree = [0] * size
seg_tree = SegmentTree(N)
res = []
for i in range(N):
    a = comp_arr[i]
    s = seg_tree.qeury(a)
    res.append(str(i + 1 - s))
    seg_tree.update(a)
    # j = a
    # s = 0
    # while j > 0:
    #     s += tree[j]
    #     j -= j & -j
    # res.append(str(i + 1 - s))
    # j = a
    # while j < size:
    #     tree[j] += 1
    #     j += j & -j
sys.stdout.write("\n".join(res))
'''
111
110
100
1 * 7 - 0
'''