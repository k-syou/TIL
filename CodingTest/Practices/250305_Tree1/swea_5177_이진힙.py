T = int(input())


class MyHeap:
    def __init__(self):
        self.heap = [-1]
        self.size = 0

    def shift_up(self, c):
        while c > 1:
            p = c // 2
            if self.heap[p] > self.heap[c]:
                self.heap[p], self.heap[c] = self.heap[c], self.heap[p]
                c = p
            else:
                break

    def heappush(self, v):
        self.heap.append(v)
        self.size += 1
        self.shift_up(self.size)

    def prefix(self, c):
        if c == 1:
            return self.heap[c]
        return self.heap[c] + self.prefix(c // 2)


for tc in range(1, T + 1):
    N = int(input())
    arr = [*map(int, input().split())]
    heap = MyHeap()
    for v in arr:
        heap.heappush(v)
    # print(heap.heap)

    print(f"#{tc} {heap.prefix(N // 2)}")
