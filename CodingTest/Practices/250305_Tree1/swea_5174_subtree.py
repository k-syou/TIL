T = int(input())


def get_subtree_cnt(child, p):
    res = 1
    for c in child[p]:
        res += get_subtree_cnt(child, c)
    return res


for tc in range(1, T + 1):
    E, N = map(int, input().split())
    child = {i + 1: [] for i in range(E + 1)}
    lines = [*map(int, input().split())]
    for i in range(0, 2 * E, 2):
        child[lines[i]].append(lines[i + 1])

    print(f"#{tc} {get_subtree_cnt(child, N)}")
