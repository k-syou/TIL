T = int(input())


def shift_down(p, tree):
    if p * 2 <= N:
        l = p * 2
        r = l + 1
        if tree[l] > tree[p]:
            tree[l], tree[p] = tree[p], tree[l]
            shift_down(l, tree)
        if r <= N and tree[r] < tree[p]:
            tree[r], tree[p] = tree[p], tree[r]
            shift_down(r, tree)


def in_order(i, tree):
    global v
    l = i * 2
    r = l + 1
    if l <= N:
        in_order(l, tree)
    tree[i] = v
    v += 1
    if r <= N:
        in_order(r, tree)


v = 1

for tc in range(1, T + 1):
    N = int(input())
    tree = [*range(N + 1)]
    size = 1
    for i in range(N // 2, 0, -1):
        shift_down(i, tree)

    print(f"#{tc} {tree[1]} {tree[N // 2]}")
