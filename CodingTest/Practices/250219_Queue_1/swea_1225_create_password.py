from collections import deque

for _ in range(10):
    tc = int(input())
    q = deque([*map(int, input().split())])
    zero = 1  # 0 숫자 발생 여부 | 1 = 0이 없음 | 0 = 발생
    while zero:
        for i in range(1, 6):  # 1 ~ 5
            v = q.popleft() - i  # q의 값
            if v <= 0:  # v 가 0보다 작은 경우
                zero = 0
                break
            # 아니라면 다시 큐에 추가
            q.append(v)

    # 마지막 0을 포함하여 출력
    print(f"#{tc}", *list(q), 0)
