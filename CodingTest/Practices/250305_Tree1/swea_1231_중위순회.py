def in_order(child, node):
    global res
    if child[node]:
        in_order(child, child[node][0])
        res += mapping[node]
        if len(child[node]) > 1:
            in_order(child, child[node][1])
    else:
        res += mapping[node]


for tc in range(1, 11):
    N = int(input())
    res = ""
    mapping = {i + 1: "" for i in range(N)}
    child = {i + 1: [] for i in range(N)}
    for _ in range(N):
        n, alpha, *childs = input().split()
        n = int(n)
        mapping[n] = alpha
        for c in childs:
            child[n].append(int(c))
    in_order(child, 1)
    print(f"#{tc} {res}")
