class queue:  # 큐 구현
    def __init__(self, N):
        self.n = N  # 최대 길이
        self.q = [None] * N  # 빈 큐 생성
        self.f = self.r = 0  # front, reer 초기화
        self.size = 0  # 현재 q의 사이즈

    def append(self, v):
        if self.size > 0 and self.r == self.f:
            # 한 바퀴 돌아서 인덱스가 초과하는 경우
            raise IndexError
        idx = self.r  # 값을 추가할 위치
        self.q[idx] = v  # 값 할당
        self.r = (self.r + 1) % self.n  # 다음 reer 위치로 설정
        self.size += 1  # 사이즈 증가

    def pop(self):
        if not self.size and self.r == self.f:
            # 더이상 출력할 요소가 없는 경우
            return None
        idx = self.f  # 값을 꺼낼 위치
        self.f = (self.f + 1) % self.n  # 다음 front 위치로 설정
        self.size -= 1  # 사이즈 감소
        return self.q[idx]  # 값 출력

    def __str__(self):
        # debug
        return f"<queue: {self.q}, front : {self.f}, reer : {self.r}>"


for tc in range(1, int(input()) + 1):
    n, m = map(int, input().split())  # n : queue의 크기 | m : 피자의 개수
    pizzas = [*map(int, input().split())]  # 피자별 치즈 양
    q = queue(n)
    i = 0
    # 초기 큐 배열값 append
    for _ in range(n):
        q.append((pizzas[i], i + 1))  # (치즈 양, 피자번호)
        i += 1
    while q.size > 1:  # 피자가 한개만 남은 경우 종료
        cheeze, idx = q.pop()  # 피자를 꺼내봄
        cheeze //= 2  # 치즈 2배 감소
        if cheeze <= 0:  # 치즈가 0 이하인 경우
            if i < m:  # 아직 남은 피자가 있는 경우
                q.append((pizzas[i], i + 1))
                i += 1
            continue
        # 아직 치즈가 0이 아닌경우
        q.append((cheeze, idx))

    # 마지막 피자의 번호 출력
    print(f"#{tc} {q.pop()[1]}")
"""
3
3 5
7 2 6 5 3
5 10
5 9 3 9 9 2 5 8 7 1
5 10
20 4 5 7 3 15 2 1 2 2
"""
