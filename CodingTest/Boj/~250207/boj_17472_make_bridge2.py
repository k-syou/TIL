from collections import deque

# 1 <= N, M <= 10
N, M = map(int, input().split())

island_map = [[*map(int, input().split())] for _ in range(N)]
dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]


def init_island(y, x, num):
    global island_map
    q = deque()
    q.append((y, x))
    loc = [[y, x]]
    island_map[y][x] = num
    while q:
        ty, tx = q.popleft()
        for i in range(4):
            ny = ty + dy[i]
            nx = tx + dx[i]
            if ny < 0 or ny >= N or nx < 0 or nx >= M:
                continue
            if island_map[ny][nx] != 1:
                continue
            island_map[ny][nx] = num
            q.append((ny, nx))
            loc.append((ny, nx))

    return loc


def get_bridges(y, x):
    start_num = island_map[y][x]
    bridges = set()
    q = deque()
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if ny < 0 or ny >= N or nx < 0 or nx >= M:
            continue
        if island_map[ny][nx]:
            continue
        q.append((y, x, i, 0))

    while q:
        ty, tx, d, dist = q.popleft()
        ny = ty + dy[d]
        nx = tx + dx[d]
        if ny < 0 or ny >= N or nx < 0 or nx >= M:
            continue
        if island_map[ny][nx]:
            if dist > 1:
                start = min(start_num, island_map[ny][nx])
                end = max(start_num, island_map[ny][nx])
                bridges.add((dist, start - 2, end - 2))
            continue
        q.append((ny, nx, d, dist + 1))
    return bridges


num = 2
islands_loc = []
for y in range(N):
    for x in range(M):
        if island_map[y][x] == 1:
            islands_loc.append(init_island(y, x, num))
            num += 1
num -= 2
# for row in island_map:
#     print(*[x - 2 if x else x for x in row])

temp_bridges = set()
for island_loc in islands_loc:
    for y, x in island_loc:
        temp_bridges = temp_bridges | get_bridges(y, x)


# 유니온 파인드 알고리즘
def find(x):
    global parent
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    global parent, rank
    rootA = find(a)
    rootB = find(b)
    if rootA != rootB:
        if rank[rootA] > rank[rootB]:
            parent[rootB] = rootA
        elif rank[rootA] < rank[rootB]:
            parent[rootA] = rootB
        else:
            parent[rootB] = rootA
            rank[rootA] += 1
        return True
    return False


edges = sorted(temp_bridges)
parent = [*range(num)]
rank = [0] * num
mst_weight = 0
connected_edges = 0

for weight, u, v in edges:
    if union(u, v):
        mst_weight += weight
        connected_edges += 1
        if connected_edges == num - 1:
            break

root = find(0)
for i in range(1, num):
    if find(i) != root:
        mst_weight = -1
        break

print(mst_weight)





#
# # print(temp_bridges)
#
# bridges_dict = {i: {} for i in range(num)}
# for bridge in temp_bridges:
#     if bridge[2] in bridges_dict[bridge[1]]:
#         bridges_dict[bridge[1]][bridge[2]] = min(bridge[0], bridges_dict[bridge[1]][bridge[2]])
#     else:
#         bridges_dict[bridge[1]][bridge[2]] = bridge[0]
#     if bridge[1] in bridges_dict[bridge[2]]:
#         bridges_dict[bridge[2]][bridge[1]] = min(bridge[0], bridges_dict[bridge[1]][bridge[2]])
#     else:
#         bridges_dict[bridge[2]][bridge[1]] = bridge[0]
#
# print(bridges_dict)
#
# visited = [False] * num
# result = 10 ** 8
#
#
# def backtrack(i, total, count):
#     global visited, result
#     if count == num:
#         result = min(result, total)
#         return
#
#     for key, value in bridges_dict[i].items():
#         if not visited[key]:
#             visited[key] = True
#             backtrack(key, total + value, count + 1)
#             visited[key] = False
#
#
# for i in range(num):
#     visited[i] = True
#     backtrack(i, 0, 1)
#     visited[i] = False
#
# if result == 10 ** 8:
#     result = -1
#
# print(result)