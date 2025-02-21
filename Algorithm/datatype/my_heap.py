class Heap:
    def __init__(self, iterator: list = []):
        self.heapify(iterator)

    def hpush(self, value):
        # 힙에 value를 추가
        self.heapappend(value)

        # 마지막 노드 정렬
        self.shift_up(self.length - 1)

    def shift_up(self, c_node):
        # 마지막 노드로 부터 부모노드와 크기를 비교하며 변경
        while c_node > 0:
            p_node = (c_node - 1) // 2
            if self._heapq[p_node] > self._heapq[c_node]:
                self._heapq[p_node], self._heapq[c_node] = (
                    self._heapq[c_node],
                    self._heapq[p_node],
                )
                # 변경이 된경우 부모노드를 자식 노드로 변경
                c_node = p_node
            else:
                break

    def heapappend(self, value):
        self._heapq.append(value)
        self.length += 1

    def hpop(self):
        if self.length == 0:
            # heap 길이가 0인 경우
            return None
        if self.length == 1:
            # heap 길이가 1인 경우
            self.length = 0
            return self._heapq.pop()

        # 제일 첫번째 값을 저장해 두고,
        # 마지막 값을 첫번째 값으로 변경
        result = self._heapq[0]
        self._heapq[0] = self._heapq.pop()
        self.length -= 1

        # 0번 노드 부터 아래로 검색하여 정렬
        self.shift_down(0)
        return result

    def shift_down(self, p_node):
        # 부모 노드로 부터 자식 노드와 비교하며
        # 자식 노드의 값이 더 작은 경우 변경 하고 재호출
        last = self.length // 2 - 1
        while p_node <= last:
            c_node = (p_node * 2) + 1
            s_node = c_node + 1
            if s_node < self.length and self._heapq[c_node] > self._heapq[s_node]:
                c_node = s_node

            if self._heapq[p_node] > self._heapq[c_node]:
                self._heapq[p_node], self._heapq[c_node] = (
                    self._heapq[c_node],
                    self._heapq[p_node],
                )
                p_node = c_node
            else:
                break

    def __str__(self):
        return f"heap : {self._heapq}"

    def heapify(self, arr):
        self.length = len(arr)
        self._heapq = arr[:]
        # 마지막 부모 노드
        last = self.length // 2 - 1
        for i in range(last, -1, -1):
            self.shift_down(i)


class MaxHeap(Heap):

    def shift_up(self, c_node):
        # 마지막 노드로 부터 부모노드와 크기를 비교하며 변경
        while c_node > 0:
            p_node = (c_node - 1) // 2
            if self._heapq[p_node] < self._heapq[c_node]:
                self._heapq[p_node], self._heapq[c_node] = (
                    self._heapq[c_node],
                    self._heapq[p_node],
                )
                # 변경이 된경우 부모노드를 자식 노드로 변경
                c_node = p_node
            else:
                break

    def shift_down(self, p_node):
        # 부모 노드로 부터 자식 노드와 비교하며
        # 자식 노드의 값이 더 큰 경우 변경 하고 재호출
        last = self.length // 2 - 1
        while p_node <= last:
            c_node = (p_node * 2) + 1
            s_node = c_node + 1
            if s_node < self.length and self._heapq[c_node] < self._heapq[s_node]:
                c_node = s_node

            if self._heapq[p_node] < self._heapq[c_node]:
                self._heapq[p_node], self._heapq[c_node] = (
                    self._heapq[c_node],
                    self._heapq[p_node],
                )
                p_node = c_node
            else:
                break


if __name__ == "__main__":
    hq = Heap()
    max_hq = MaxHeap()
    # hq = Heap([])

    for i in range(3):
        for j in range(3):
            hq.hpush((j, i))
            max_hq.hpush((j, i))

    while hq.length:
        print(hq.hpop())
        print(hq)
    while max_hq.length:
        print(max_hq.hpop())
        print(max_hq)
