def preprocess_bad_character(pattern):
    bad_char = {}
    for i, char in enumerate(pattern):
        bad_char[char] = i
    return bad_char


def print_p(g, b, pattern, i, j):
    arrow = [" "] * (len(pattern) + 2)
    print("good_suffix")
    print(*range(len(pattern) + 1))
    print(*g)
    print("-----------------------")

    print("border")
    print(*range(len(pattern) + 1))
    print(*b)
    print("-----------------------\n")
    print(*range(len(pattern) + 1))
    print(*pattern)
    arrow[i - 1] = "I"
    arrow[j - 1] = "J"
    print(*arrow)
    print()


def preprocess_good_suffix(pattern):
    """
    좋은 접미사 규칙(Good Suffix Rule)을 위한 이동 테이블(good_suffix)을 생성합니다.
    good_suffix[i]는 패턴에서 인덱스 i-1에서 불일치가 발생했을 때,
    패턴을 오른쪽으로 얼마만큼 이동시켜야 하는지를 나타냅니다.

    아래 알고리즘은 border(경계) 정보를 이용하여, 패턴의 각 접미사가
    패턴 내부에서 다시 나타나는 위치(또는 접두사와 일치하는 정도)를 계산합니다.
    """
    m = len(pattern)
    good_suffix = [m] * (m + 1)
    border = [0] * (m + 1)

    i = m  # i = 패턴의 길이
    j = m + 1  # j = 패턴의 길이 + 1
    border[i] = j  # border의 마지막 요소 = j
    while i > 0:  # i = m ~ 1
        print_p(good_suffix, border, pattern, i, j)
        while j <= m and pattern[i - 1] != pattern[j - 1]:  # j <= 패턴의 길이
            if good_suffix[j] == m:  # good_suffix 가 기본값(m)일 때
                good_suffix[j] = j - i  # j 위치에 j - i 를 할당
            j = border[j]  # j에 border[j]를 할당
            print_p(good_suffix, border, pattern, i, j)
        i -= 1
        j -= 1
        border[i] = j
        print(f"border[{i}] = {j}")

    j = border[0]
    for i in range(m + 1):
        if good_suffix[i] == m:
            good_suffix[i] = j
        if i == j:
            j = border[j]

    return good_suffix


def boyer_moore_search(text, pattern):
    """
    Boyer-Moore 문자열 검색 알고리즘.
    텍스트(text) 내에서 패턴(pattern)이 등장하는 모든 시작 인덱스를 리스트로 반환합니다.
    """
    n = len(text)
    m = len(pattern)
    if m == 0:
        return []  # 빈 패턴은 검색하지 않음

    # 사전 처리: 두 가지 규칙에 대한 테이블 생성
    bad_char = preprocess_bad_character(pattern)
    good_suffix = preprocess_good_suffix(pattern)

    occurrences = []  # 패턴이 나타나는 시작 인덱스를 저장할 리스트
    s = 0  # 텍스트 내에서의 현재 패턴의 위치(shift)

    while s <= n - m:
        j = m - 1  # 패턴의 마지막 문자부터 비교 시작

        # 오른쪽에서 왼쪽으로 패턴과 텍스트를 비교합니다.
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1

        if j < 0:
            # 패턴과 텍스트가 완전히 일치함: s 위치에 패턴이 존재
            occurrences.append(s)
            # 전체 패턴이 일치한 경우에도, good_suffix[0]만큼 이동(0이 될 수 있으므로 최소 1)
            s += good_suffix[0] if good_suffix[0] > 0 else 1
        else:
            # 불일치가 발생한 경우, 두 규칙에 따라 이동 거리를 계산합니다.
            # (1) 나쁜 문자 규칙: 불일치한 텍스트 문자(text[s+j])가 패턴 내 마지막에 등장한 위치를 이용
            bc_shift = j - bad_char.get(text[s + j], -1)
            # (2) 좋은 접미사 규칙: 미리 계산된 이동 값 사용 (인덱스 j+1 사용)
            gs_shift = good_suffix[j + 1]
            # 두 규칙 중 큰 값만큼 이동
            s += max(bc_shift, gs_shift)
    return occurrences


# print(preprocess_bad_character("abcdabcef"))
print(preprocess_good_suffix("ababaaa"))
