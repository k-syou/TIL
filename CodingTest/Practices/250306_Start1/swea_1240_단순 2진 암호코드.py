import sys

sys.stdin = open("1240_input.txt", "r")

T = int(input())

PASSWORD = {
    "0001101": 0,
    "0011001": 1,
    "0010011": 2,
    "0111101": 3,
    "0100011": 4,
    "0110001": 5,
    "0101111": 6,
    "0111011": 7,
    "0110111": 8,
    "0001011": 9,
}

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    table = [input() for _ in range(N)]
    password_list = []
    for y in range(N):
        # "1"이 없는 경우 해당 열은 확인 하지 않음
        if "1" not in table[y]:
            continue
        p = 0
        # 모든 숫자는 맨 뒤에 1을 포함하므로 뒤에서부터 검사하여
        # 비밀번호 끝 위치 찾기
        for x in range(M - 1, 6, -1):
            if table[y][x] == "1":
                p = x
                break
        # 비밀번호 8개 추출
        for _ in range(8):
            password_list.append(PASSWORD[table[y][p - 6 : p + 1]])
            p -= 7
        break
    # 뒤에서부터 확인하여 password 리스트는 역순으로 저장되어있으므로
    # 짝수 인덱스 : 0, 2, ..
    # 홀수 인덱스 : 1, 3, ..

    # check = ((홀수번 번호 * 3 의 합) + (짝수번 번호의 합)) % 10
    check = (
        sum(map(lambda x: x * 3, password_list[1::2])) + sum(password_list[::2])
    ) % 10
    if check > 0:
        # check 값이 0이 아닌경우 10의 배수가 아니므로
        result = 0
    else:
        # 올바른 암호코드이므로 모든 번호들의 합을 result에 담음
        result = sum(password_list)
    print(f"#{tc} {result}")
