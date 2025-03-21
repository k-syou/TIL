class Fenw:
    def __init__(self, N):
        self.tree = [0] * (N + 1)
        self.size = N
    
    def update(self, i, k):
        while i <= self.size:
            self.tree[i] ^= k
            i += i & -i
        print(self.tree)
    
    def query(self, i, j):
        print(self.tree)
        tot_i = 0
        tot_j = 0
        while self.size >= i > 0:
            print(i, bin(i))
            tot_i += self.tree[i]
            i -= i & -i
        while self.size >= j > 0:
            print(j, bin(j))
            tot_j += self.tree[j]
            j -= j & -j
        print(tot_i, tot_j)
        return tot_j - tot_i
            
        

N, M = map(int, input().split())
fenw = Fenw(N)
for i in range(M):
    o, s, t = map(int, input().split())
    if o == 0:
        fenw.update(s, 1)
        if t + 1 < N:
            fenw.update(t + 1, 1)
    else:
        print(fenw.query(s - 1, t))