import heapq


def run_():
    q = [(-1, 0)]  # 우선순위 큐 사용
    while q:
        # 이동횟수(cnt)가 작고 같다면 멀리 있는 위치(i) 부터 검색
        cnt, i = heapq.heappop(q)
        i = -i  # 양수로 변경
        if i >= N - 1:
            # 최종 목적지에 도착한 경우
            return cnt
        for j in range(i + 1, i + 1 + M[i]):
            # 해당 위치에서 갈수 있는 모든 위치 담기
            heapq.heappush(q, (cnt + 1, -j))


T = int(input()) + 1
for tc in range(1, T):
    N, *M = map(int, input().split())
    res = run_()
    print(f"#{tc} {res}")