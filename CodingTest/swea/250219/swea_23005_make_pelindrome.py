def is_x_pelindrome(s):
    """
    'x' 를 추가하여 회문의 형태로 만들 수 있는지 확인하고
    최소 몇개의 'x'가 필요한지 확인한다.

    res: 'x'의 필요 개수
    추가해도 회문의 형태가 되지 않으면 -1을 리턴한다.
    가능하다면 res를 리턴한다.
    """
    n, res = len(s), 0
    i, j = 0, n - 1  # 문자의 양끝 인덱스
    while i <= j:
        # i가 앞쪽 인덱스, j가 뒤쪽 인덱스임을 만족할 때(i <= j) 반복
        if s[i] == s[j]:
            # 양 끝이 같은 값인 경우 포인터를 안쪽으로 1만큼 변경
            i += 1
            j -= 1
        elif s[i] == "x":
            # 다른 경우, 앞쪽이 x이면
            # 뒤쪽에 'x'를 하나 추가했다 가정후에
            # 앞쪽 포인터를 안쪽으로 1만큼 변경
            i += 1
            res += 1
        elif s[j] == "x":
            # 위와 동일하게 뒤쪽이 x 이면
            # 앞쪽에 'x'를 하나 추가했다 가정후,
            # 뒤쪽 포인터를 안쪽으로 1만큼 변경
            j -= 1
            res += 1
        else:
            # 모든 조건을 만족하지 못하는 경우
            # 회문으로 만들 수 없으므로 -1 리턴
            return -1
    return res


for _ in range(int(input())):
    print(is_x_pelindrome(input()))
