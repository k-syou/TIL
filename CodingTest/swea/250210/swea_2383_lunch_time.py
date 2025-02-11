T = int(input())


def get_distance(people, stairway):
    # 거리 계산산
    return abs(people[0] - stairway[0]) + abs(people[1] - stairway[1])


def simulate(people, stairway):
    from collections import deque

    stairway_q = deque()
    # 현재 시간
    time = 0
    # 사람 index
    idx = 0
    # 계단의 길이
    k = stairway[2]
    # 거리순으로 정렬
    people_dist = sorted(get_distance(p, stairway) for p in people)

    while stairway_q or idx < len(people):
        time += 1

        # 현재 계단에 있는 사람이 있고, 도착시간이 된 경우
        while stairway_q and stairway_q[0] == time:
            # 계단에 있는 사람을 뺌
            stairway_q.popleft()

        # 모든 인원이 계단에 올라가지 않고, 계단에 있는 사람의 인원 수가 3 미만일 때
        while idx < len(people) and len(stairway_q) < 3:
            # 현재 시간이 제일 짧은 시간안에 오는 사람의 거리(시간) + 1(기다리는 시간)
            # 보다 크다면 계단 입장
            if people_dist[idx] + 1 <= time:
                stairway_q.append(time + k)
                idx += 1
            else:
                break

    return time


def find_min_time(people, stairways):
    people_count = len(people)
    min_time = float("inf")

    for i in range(1 << (people_count + 1)):
        # 완전탐색, 비트마스킹
        # 1 <= people_count <= 10
        # 최대 2 ** 10 = 1024 번 반복
        group1 = [people[j] for j in range(people_count) if i & (1 << j) == 0]
        group2 = [people[j] for j in range(people_count) if i & (1 << j)]

        # 1번 그룹 및 2번 그룹의 총 소요 시간 확인
        time1 = simulate(group1, stairways[0])
        time2 = simulate(group2, stairways[1])

        # 1번 그룹 과 2번 그룹의 총 소요시간의 최대값과 결과 최소값 중 짧은 시간 할당
        min_time = min(min_time, max(time1, time2))
    return min_time


for tc in range(1, T + 1):
    N = int(input())
    grid = [[*map(int, input().split())] for _ in range(N)]
    people = []
    stairway = []
    for y in range(N):
        for x in range(N):
            if grid[y][x] == 1:
                # 사람의 위치
                people.append((y, x))
            if grid[y][x] >= 2:
                # 계단의 위치 + 계단의 길이
                stairway.append((y, x, grid[y][x]))
    min_time = find_min_time(people, stairway)
    print(f"#{tc} {min_time}")
