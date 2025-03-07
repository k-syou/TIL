import sys

sys.stdin = open("1242_input.txt", "r")

# HEX = {str(i): i for i in range(10)}
# for i, x in enumerate("ABCDEF"):
#     HEX[x] = 10 + i

# PASSWORD = {
#     "0001101": 0,
#     "0011001": 1,
#     "0010011": 2,
#     "0111101": 3,
#     "0100011": 4,
#     "0110001": 5,
#     "0101111": 6,
#     "0111011": 7,
#     "0110111": 8,
#     "0001011": 9,
# }

"""
1. 행 단위로 검사
2. 행에 0만 채워져 있거나, 전 행과 같은 경우는 체크하지 않음
3. 각 셀의 값이 16진수라고 했을 때, 행 단위로 2진수로 변경(xxxx(4자리씩))
4. 맨 오른쪽 1의 위치를 찾고 끝에서 부터 3개의 패턴을 찾고,
    패턴별 길이의 최소값을 구함(압축할 크기)
5. 압축할 크기 * 56 까지의 크기만큼의 배열을 해독
6. 해독한 번호가 이미 해독한 번호면 결과 값에 누적하지 않고 넘김
7. 해당 배열만큼을 제외하고 왼쪽에 값이 더 있는 경우 4번부터 반복
8. 다음 행 검사(4번부터 반복)
9. 출력
"""

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


def hex_to_bin(hex_str):
    # ch : 셀의 값(16진수)
    # bin(int(ch, 16))[2:].zfill(4) : 16진수 값을 4자리 2진수 값으로 변경
    return "".join(bin(int(ch, 16))[2:].zfill(4) for ch in hex_str)


T = int(input())
result_all = []
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    board = [input().strip() for _ in range(N)]
    result = 0
    found_codes = set()  # 중복 암호코드 방지를 위한 집합

    # 행 단위 검사
    for i in range(N):
        # 해당 행이 모두 '0'이면 넘어감
        if set(board[i]) == {"0"}:
            continue
        if i > 0 and board[i] == board[i - 1]:
            continue

        # 행 16진수 -> 2진수로 변경
        bin_line = hex_to_bin(board[i])

        # j : 맨 뒤 index
        j = len(bin_line) - 1
        while j >= 55:  # 암호코드 최소 길이 56비트가 필요하므로 55 미만인 경우에 종료
            # pos : 0 ~ j 범위 내에서 가장 오른쪽 1의 위치
            pos = bin_line.rfind("1", 0, j + 1)

            if pos == -1:
                # 없는 경우 열 검사 종료
                break

            # pos 위치에서부터 3개의 패턴을 보고 그 패턴의 최소값이
            # 배율(v) 이라는 것을 알 수있음
            # 한 비밀번호의 규칙이 c1 : c2 : c3 : c4 라고 할때,
            # c2 : c3 : c4 에 무조건 비율이 1인 값이 있으므로 3개만 확인
            c4 = c3 = c2 = 0
            k = pos
            while k >= 0 and bin_line[k] == "1":
                c4 += 1
                k -= 1
            while k >= 0 and bin_line[k] == "0":
                c3 += 1
                k -= 1
            while k >= 0 and bin_line[k] == "1":
                c2 += 1
                k -= 1

            if c2 == 0 or c3 == 0 or c4 == 0:
                # 검사도중 범위를 초과한 경우
                j = pos - 1
                continue
            # 배율 구하기
            v = min(c2, c3, c4)

            total_length = 56 * v  # 전체 암호코드 길이
            start = pos - total_length + 1  # 암호 시작 위치
            if start < 0:
                # 시작 위치가 범위를 벗어난 경우
                j = pos - 1
                continue

            # 검사할 범위 지정
            code_segment = bin_line[start : pos + 1]

            # 56×v 길이의 구간을 8자리로 나누어 디코딩
            digits = []  # 결과 숫자를 담을 list
            valid = True  # 수행 결과
            for d in range(8):
                seg_start = d * 7 * v
                seg_end = (d + 1) * 7 * v
                # 8개의 숫자중 하나의 구간(2진수)
                segment = code_segment[seg_start:seg_end]
                # 각 숫자에 대해, v단위로 압축하여 7비트 패턴 구하기
                # 반복되는 숫자의 맨 앞자리만 추출하여 압축
                pattern = "".join(segment[j * v] for j in range(7))

                # 해당 패턴이 비밀번호안에 있는지 확인
                if pattern in PASSWORD:
                    digits.append(PASSWORD[pattern])
                else:
                    # 없는 경우 실패 처리
                    valid = False
                    break

            if valid:
                # 검증코드 체크: 홀수 자리 3배, 짝수 자리 그대로 합산
                checksum = 0
                for idx, digit in enumerate(digits):
                    if idx % 2 == 0:
                        checksum += digit * 3
                    else:
                        checksum += digit

                # 10의 배수인지 확인
                if checksum % 10 == 0:
                    code_tuple = tuple(digits)
                    # 중복되지 않은 암호코드만 결과에 누적
                    if code_tuple not in found_codes:
                        result += sum(digits)
                        found_codes.add(code_tuple)
            # 다음 탐색은 현재 암호 코드 시작 전까지 진행
            j = start - 1

    result_all.append(f"#{tc} {result}")

print(*result_all, sep="\n")


# def hex_pass_to_bin_pass(hex_pass):
#     bin_pass = ""
#     for c in hex_pass:
#         t = bin(HEX[c]).replace("0b", "").zfill(4)
#         bin_pass += t
#     return bin_pass


# def get_v(hex_pass):
#     bin_pass = zfill_bin(hex_pass_to_bin_pass(hex_pass))
#     # print(bin_pass)
#     v = float("inf")
#     check = 0
#     x = "0"
#     first = True
#     for i in range(len(bin_pass)):
#         if x == bin_pass[i]:
#             check += 1
#         else:
#             if not first:
#                 # print(check)
#                 v = min(v, check)
#             first = False
#             x = bin_pass[i]
#             check = 1
#     return v


# def zfill_bin(bin_pass):
#     lst = [*bin_pass]
#     # n = len(lst)
#     while lst[-1] == "0":
#         lst.pop()
#     result = "".join(lst)
#     return result


# def bin_pass_decoding(bin_pass, v):
#     # print(bin_pass, v)
#     N = len(bin_pass)
#     scan_password = []
#     for i in range(N - 1, -1, -1):
#         if bin_pass[i] == "1":
#             bin_pass = bin_pass[: i + 1]
#             bin_pass = bin_pass.zfill(56 * v)
#             if len(bin_pass) > 56 * v:
#                 bin_pass = bin_pass[len(bin_pass) - 56 * v :]
#                 # print(len(bin_pass))
#             break
#     # print(bin_pass)
#     for i in range(0, 56 * v, v * 7):
#         key = ""
#         for j in range(7):
#             # print(i + j * v, bin_pass[i + j * v])
#             key += bin_pass[i + j * v]
#         # print(key)
#         scan_password.append(PASSWORD[key])

#     return scan_password


# def check_password(scan_password):
#     tot = 0
#     result = sum(scan_password)
#     for i in range(8):
#         if i % 2:
#             # 짝수 번째 숫자
#             tot += scan_password[i]
#         else:
#             # 홀수 번째 숫자
#             tot += scan_password[i] * 3
#     print(tot)
#     if tot % 10:
#         result = 0
#     return result


# T = int(input())
# output = []
# for tc in range(1, T + 1):
#     N, M = map(int, input().split())
#     # hex_pass_set = set()
#     hex_pass_lst = []
#     password_code = [input() for _ in range(N)]
#     visited = [[0] * M for _ in range(N)]
#     for r in range(N):
#         if set(password_code[r]) == {"0"}:
#             continue
#         c = M - 1
#         bit_cnt = 0
#         hex_code = ""
#         is_first = True
#         while c >= 0:
#             if visited[r][c]:
#                 c -= 1
#                 continue
#             if password_code[r][c] != "0":
#                 if is_first:
#                     is_first = False
#                     bin_tmp = bin(HEX[password_code[r][c]])
#                     if bin_tmp[-1] != "1":
#                         bit_cnt -= 4
#                 for i in range(r, N):
#                     if password_code[r][c] != password_code[i][c]:
#                         break
#                     visited[i][c] = 1
#                 bit_cnt += 4
#                 hex_code = password_code[r][c] + hex_code
#             else:
#                 if bit_cnt > 0 and bit_cnt % 56:
#                     bit_cnt += 4
#                     hex_code = password_code[r][c] + hex_code
#                 else:
#                     if is_first:
#                         c -= 1
#                         continue
#                     v = get_v(hex_code)
#                     if bit_cnt == 56 * v:
#                         # hex_pass_set |= {hex_code}
#                         hex_pass_lst.append(hex_code)
#                         hex_code = ""
#                         bit_cnt = 0
#                         is_first = True
#                     else:
#                         bit_cnt += 4
#                         hex_code = password_code[r][c] + hex_code
#             c -= 1

#     result = 0
#     check_value = 0
#     # print(hex_pass_set)
#     # print(f"#{tc}-------------------------------")
#     # for hex_pass in hex_pass_set:
#     for hex_pass in hex_pass_lst:
#         # print("-----------------------")
#         # try:
#         #     bin_pass = hex_pass_to_bin_pass(hex_pass)
#         #     v = get_v(hex_pass)
#         #     scan_password = bin_pass_decoding(bin_pass, v)
#         #     check_value = check_password(scan_password, v)
#         #     if check_value:
#         #         result = check_value
#         #         break
#         # except:
#         #     continue
#         if not hex_pass:
#             continue
#         print(hex_pass)
#         bin_pass = hex_pass_to_bin_pass(hex_pass)
#         # print(bin_pass)
#         v = get_v(hex_pass)
#         # print(v)
#         scan_password = bin_pass_decoding(bin_pass, v)
#         # print(scan_password)
#         check_value = check_password(scan_password)
#         if check_value:
#             # print(hex_pass)
#             result += check_value
#     output.append(f"#{tc} {result}")
#     # print(f"#{tc} {result}")

# print(*output, sep="\n")
