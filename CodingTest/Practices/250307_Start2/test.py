HEX = {str(i): i for i in range(10)}
for i, x in enumerate("ABCDEF"):
    HEX[x] = 10 + i

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

s = "0C99624DDAF324C"


def hex_pass_to_bin_pass(hex_pass):
    bin_pass = ""
    for c in hex_pass:
        t = bin(HEX[c]).replace("0b", "").zfill(4)
        bin_pass += t
    return bin_pass


def bin_pass_decoding(bin_pass):
    print(bin_pass)
    N = len(bin_pass)
    v = N // 56
    for i in range(len(bin_pass) - 1, -1, -1):
        if bin_pass[i] == "1":
            bin_pass = bin_pass[i - v * 56 + 1 : i + 1]
            break
    print(bin_pass)
    scan_password = []
    for i in range(0, len(bin_pass), v * 7):
        key = ""
        for j in range(7):
            key += bin_pass[i + j * v]
        scan_password.append(PASSWORD[key])

    return scan_password


def check_password(scan_password):
    print(scan_password)
    tot = 0
    result = 0
    for i in range(8):
        if i % 2:
            # 짝수 번째 숫자
            tot += scan_password[i]
        else:
            # 홀수 번째 숫자
            tot += scan_password[i] * 3
        result += scan_password[i]
    print(tot)
    if tot % 10:
        result = 0
    return result


def get_v(hex_pass):
    bin_pass = zfill_bin(hex_pass_to_bin_pass(hex_pass))
    print(bin_pass)
    v = float("inf")
    check = 0
    x = "0"
    first = True
    for i in range(4, len(bin_pass)):
        if x == bin_pass[i]:
            check += 1
        else:
            if not first:
                print(check)
                v = min(v, check)
            first = False
            x = bin_pass[i]
            check = 1
    return v


def zfill_bin(bin_pass):
    lst = [*bin_pass]
    n = len(lst)
    while lst[-1] == "0":
        lst.pop()
    result = "".join(lst).zfill(n)
    return result


s = "819E79F981E1E18"
print(get_v(s))

# print(hex_pass_to_bin_pass(s))
# print(len(s))
# print(hex_pass_to_bin_pass(s))
# print(bin_pass_decoding(hex_pass_to_bin_pass(s)))
# lst = bin_pass_decoding(hex_pass_to_bin_pass(s))
# print(check_password(lst))
