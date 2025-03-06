# for i in range(1, 14):
#     print(2**-i)

m_BIN = {}


def get_m_bin(i, bin_s, dec):
    # O(2^12) = O(1)
    global m_BIN
    # 12자리까지 표기할 수 있는 모든 수(10진수)를 Key값으로
    # 소수점 아래 2진수 표기를 value 설정
    if i > 13:
        return
    # 이진수의 맨마지막 수가 '1' 인 경우에만 업데이트
    if bin_s and bin_s[-1] == "1":
        m_BIN[str(dec)] = bin_s
    # '0'과 '1'분기 처리
    get_m_bin(i + 1, bin_s + "0", dec)
    get_m_bin(i + 1, bin_s + "1", dec + 2**-i)


get_m_bin(1, "", 0)

for tc in range(1, int(input()) + 1):
    x = input()
    if x not in m_BIN:
        # key 값에 없으면 "overflow"
        result = "overflow"
    else:
        result = m_BIN[x]
    print(f"#{tc} {result}")
