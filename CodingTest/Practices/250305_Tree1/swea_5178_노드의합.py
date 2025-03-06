T = int(input())


def prefix(tree, n):
    if tree[n] != -1:
        return tree[n]
    l = n * 2
    r = l + 1
    tree[n] = prefix(tree, l)
    if r <= N:
        tree[n] += prefix(tree, r)
    return tree[n]


for tc in range(1, T + 1):
    N, M, L = map(int, input().split())
    tree = [-1] * (N + 1)
    for _ in range(M):
        node, value = map(int, input().split())
        tree[node] = value

    print(f"#{tc} {prefix(tree, L)}")
