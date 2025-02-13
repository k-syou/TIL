def kmp(t, p):
    n = len(t)
    m = len(p)

    # table 생성
    lps = [0] * (m + 1)
    lps[0] = -1
    j = 0
    for i in range(1, m):
        lps[i] = j
        if p[i] == p[j]:
            j += 1
        else:
            j = 0
    lps[m] = j

    # 비교
    i = j = 0
    while i < n and j <= m:
        if j == -1 or t[i] == p[j]:
            i += 1
            j += 1
        else:
            j = lps[j]
        if j == m:
            print(i - m, end=" ")
            j = lps[j]


kmp("aaaaaaaaaaab", "ab")
