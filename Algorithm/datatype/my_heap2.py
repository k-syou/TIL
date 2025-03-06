class Heap:
    def __init__(self, arr=[]):
        self._heap = [None] + arr
        self._size = len(arr)
        self.heapify()

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, x: int):
        self._size = x
        # self.size += x

    @property
    def heap(self):
        return self._heap

    def shift_down(self, p_node):
        while p_node < self.size:
            c_node1 = p_node * 2
            c_node2 = c_node1 + 1
            if c_node2 > self.size:
                if c_node1 > self.size:
                    return
                else:
                    c_node2 = c_node1
            min_node = c_node1 if self.heap[c_node1] <= self.heap[c_node2] else c_node2
            if self.heap[min_node] < self.heap[p_node]:
                self.heap[min_node], self.heap[p_node] = (
                    self.heap[p_node],
                    self.heap[min_node],
                )
                p_node = min_node
            else:
                return

    def shift_up(self, c_node):
        while c_node > 1:
            p_node = c_node // 2
            if self.heap[p_node] > self.heap[c_node]:
                self.heap[c_node], self.heap[p_node] = (
                    self.heap[p_node],
                    self.heap[c_node],
                )
                c_node = p_node
            else:
                break

    def heappush(self, v):
        self.heap.append(v)
        self.size += 1
        self.shift_up(self.size)

    def heappop(self):
        if self.size < 1:
            return None
        if self.size == 1:
            self.size -= 1
            return self.heap.pop()
        res = self.heap[1]
        last_v = self.heap.pop()
        self.heap[1] = last_v
        self.size -= 1
        self.shift_down(1)
        return res

    def heapify(self):
        p_size = 1
        while p_size * 2 < self.size:
            p_size *= 2

        for i in range(p_size, 0, -1):
            self.shift_down(i)

    def __str__(self):
        return f"{self.heap[1:]}"


if __name__ == "__main__":
    hq = Heap([3, 4, 5, 2, 1])
    hq.heappush(6)
    hq.heappush(9)
    hq.heappush(8)
    print(hq)
    while hq.size:
        print(hq.heappop())
