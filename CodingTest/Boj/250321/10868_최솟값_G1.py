import sys
input = sys.stdin.readline

class MinSegmentTree:
    MAX = 10e9 + 1
    def __init__(self, arr, N):
        self.n = N
        self.set_tree(arr)
    
    def set_tree(self, arr):
        # 트리 만들기
        
        # 사이즈 설정
        self.size = 1
        while self.size <= self.n:
            self.size *= 2
        self.tree = [self.MAX] * (self.size * 2)
        
        # 리프노드 최소값 설정
        for i in range(self.n):
            self.tree[self.size + i] = arr[i]
        self.get_min_value(1)

    def get_min_value(self, p_idx):
        # 탑다운 방식으로 최소값 갱신
        l = p_idx * 2
        r = l + 1
        if l < self.size * 2:
            self.tree[p_idx] = min(self.tree[p_idx], self.get_min_value(l))
        if r < self.size * 2:
            self.tree[p_idx] = min(self.tree[p_idx], self.get_min_value(r))
        return self.tree[p_idx]
    
    def query(self, a, b):
        # 바텀업 방식으로 범위 최소값 찾기
        l = a - 1 + self.size
        r = b - 1 + self.size
        res = self.MAX
        while l <= r:
            if l % 2:
                res = min(res, self.tree[l])
                l += 1
            if r % 2 == 0:
                res = min(res, self.tree[r])
                r -= 1
            l //= 2
            r //= 2
        return res
            
            
# N = 정수의 개수
# M = a ~ b 범위의 개수
N, M = map(int, input().split())
# arr = 정수의 배열
arr = [int(input()) for _ in range(N)]
# 최소값 세그먼트 트리 생성
seg_tree = MinSegmentTree(arr, N)
res = []
for _ in range(M):
    # 범위 받아오기
    a, b = map(int, input().split())
    # 쿼리 진행
    res.append(seg_tree.query(a, b))

print(*res, sep='\n')