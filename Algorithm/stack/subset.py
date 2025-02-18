def subset(arr):
    N = len(arr)
    out = [False] * N
    res = []

    def f(idx):
        nonlocal res, out
        if idx == N:
            res.append([arr[i] for i in range(N) if out[i]])
            return
        else:
            out[idx] = False
            f(idx + 1)
            out[idx] = True
            f(idx + 1)

    f(0)
    res.sort()
    return sorted(res, key=len)[1:]


print(subset([1, 2, 3, 4, 5]))
