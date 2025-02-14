# 17471, 게리맨더링
from collections import deque


def searching(group, areas, people):
    # 그룹이 연결이 되어있는지 확인하고
    # 연결된 총 선거구의 인원수를 출력
    if not group:  # 그룹이 비어있는 경우 return -1
        return -1
    q = deque()
    q.append(group[0])
    visited = {g: False for g in group}
    visited[group[0]] = True

    # 그룹 연결 상태 검색(bfs)
    while q:
        area_num = q.pop()
        for na in areas[area_num]:
            if na not in group:
                continue
            if visited[na]:
                continue
            visited[na] = True
            q.append(na)

    # 인원수 및 연결상태 확인
    res = 0
    for g in group:
        if not visited[g]:
            return -1
        res += people[g]
    return res


def soultion(people, areas, N):
    res = float("inf")

    # 간선을 나눌수 있는 모든 경우(완전탐색, 비트마스킹)
    for i in range(1 << N + 1):
        # 두개의 그룹으로 나눔
        group1 = [p + 1 for p in range(N) if i & (1 << p) > 0]
        group2 = [p + 1 for p in range(N) if i & (1 << p) == 0]
        # print("\n", i)
        # print(group1, group2)

        # 두개의 그룹이 연결 가능한지 확인 하고, 구역의 인구수를 출력
        # 연결이 불가능하면 -1 이 나옴
        cnt1 = searching(group1, areas, people)
        if cnt1 < 0:
            continue
        cnt2 = searching(group2, areas, people)
        if cnt2 < 0:
            continue

        # 두 그룹이 각자 연결이 가능할 때
        # 두 그룹의 인구수의 차이값을 res 값과 비교
        res = min(res, abs(cnt1 - cnt2))

    # 가능한 구역이 없는 경우
    if res == float("inf"):
        res = -1

    return res


# 선거구의 개수(N)
N = int(input())

# 선거구별 인원수
people = {i + 1: v for i, v in enumerate(map(int, input().split()))}

# 선거구별 간선 정보
areas = {i + 1: set() for i in range(N)}

# 간선 정보 할당
for i in range(1, N + 1):
    c, *p = map(int, input().split())
    for j in range(c):
        areas[i] |= {p[j]}

print(soultion(people, areas, N))
