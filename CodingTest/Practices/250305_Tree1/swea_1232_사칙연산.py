def tree_cal(node):
    global mapping, child
    if isinstance(mapping[node], int) or isinstance(mapping[node], float):
        return mapping[node]
    l = child[node][0]
    r = child[node][1]
    if mapping[node] == "+":
        return tree_cal(l) + tree_cal(r)
    elif mapping[node] == "-":
        return tree_cal(l) - tree_cal(r)
    elif mapping[node] == "*":
        return tree_cal(l) * tree_cal(r)
    else:
        return tree_cal(l) / tree_cal(r)


for tc in range(1, 11):
    N = int(input())
    mapping = {}
    child = {i + 1: [] for i in range(N)}
    for _ in range(N):
        node, *data = input().split()
        node = int(node)
        if data[0].isdigit():
            mapping[node] = int(data[0])
        else:
            mapping[node] = data[0]
            for c in data[1:]:
                child[node].append(int(c))

    res = int(tree_cal(1))
    print(f"#{tc} {res}")
