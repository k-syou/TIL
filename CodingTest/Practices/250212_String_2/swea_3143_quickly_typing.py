# 3143. 가장 빠른 문자열 타이핑


def preprocess_bad_character(pattern):
    bad_char = {}
    for i, char in enumerate(pattern):
        bad_char[char] = i
    return bad_char


def preprocess_good_suffix(pattern):
    m = len(pattern)

    good_suffix = [m] * (m + 1)
    border = [0] * (m + 1)

    i = m
    j = m + 1
    border[i] = j
    while i > 0:
        while j <= m and pattern[i - 1] != pattern[j - 1]:
            if good_suffix[j] == m:
                good_suffix[j] = j - i
            j = border[j]
        i -= 1
        j -= 1
        border[i] = j

    j = border[0]
    for i in range(m + 1):
        if good_suffix[i] == m:
            good_suffix[i] = j
        if i == j:
            j = border[j]
    return good_suffix


def boyer_moore_search(text, pattern):
    n = len(text)
    m = len(pattern)
    if m == 0:
        return []
    bad_char = preprocess_bad_character(pattern)
    good_suffix = preprocess_good_suffix(pattern)

    occurrences = []
    s = 0

    while s <= n - m:
        j = m - 1

        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1

        if j < 0:
            occurrences.append(s)
            s += good_suffix[0] if good_suffix[0] > 0 else 1
        else:
            bc_shift = j - bad_char.get(text[s + j], -1)
            gs_shift = good_suffix[j + 1]
            s += max(bc_shift, gs_shift)
    return occurrences


for tc in range(1, int(input()) + 1):
    A, B = input().split()
    N, M = len(A), len(B)
    i = j = 0
    occ = boyer_moore_search(A, B)
    cnt = 0
    while i < N:
        if i in occ:
            i += M
        else:
            i += 1
        cnt += 1

    print(f"#{tc} {cnt}")
