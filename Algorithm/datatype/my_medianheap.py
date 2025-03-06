import heapq


class MedianHeap:
    def __init__(self):
        # 최대 힙: 음수 값으로 저장 (실제 최대값은 -max_heap[0])
        self.max_heap = []
        # 최소 힙: 일반 값 저장
        self.min_heap = []

    def add(self, value):
        # 중앙값 유지 방법: 먼저 최대 힙에 넣고, 최대 힙의 루트를 최소 힙으로 이동, 균형 맞춤
        heapq.heappush(self.max_heap, -value)
        heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        if len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def get_median(self):
        return -self.max_heap[0] if self.max_heap else None

    def pop_max(self):
        # 최대 힙의 루트를 pop (실제 최대값)
        if not self.max_heap:
            return None
        return -heapq.heappop(self.max_heap)

    def pop_min(self):
        # 최소 힙의 루트를 pop
        if not self.min_heap:
            return None
        return heapq.heappop(self.min_heap)

    def push_max(self, value):
        # 최대 힙에 value 삽입
        heapq.heappush(self.max_heap, -value)

    def push_min(self, value):
        # 최소 힙에 value 삽입
        heapq.heappush(self.min_heap, value)

    def rebalance(self):
        # 두 힙의 균형 조정 (최대 힙이 항상 크거나 같도록)
        if len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
        elif len(self.max_heap) > len(self.min_heap) + 1:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))


# 예시: 그룹 A와 그룹 B의 중앙값 자료구조
groupA = MedianHeap()
groupB = MedianHeap()

# 각 그룹에 몇 개의 값을 넣음
for val in [10, 20, 30]:
    groupA.add(val)
for val in [5, 15, 25]:
    groupB.add(val)

# 그룹 A의 최대값과 그룹 B의 최소값 교환하기
max_A = groupA.pop_max()  # 그룹 A의 최대값 (예: 30)
min_B = groupB.pop_min()  # 그룹 B의 최소값 (예: 5)
print(max_A, min_B)
# 교환 후 삽입: 그룹 A에선 min_B, 그룹 B에선 max_A
groupA.add(min_B)
groupB.add(max_A)

# 각 그룹의 중앙값 확인
print("Group A median:", groupA.get_median())
print("Group B median:", groupB.get_median())
