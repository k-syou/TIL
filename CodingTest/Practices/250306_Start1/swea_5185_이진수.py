T = int(input())
HEX = {str(i): i for i in range(10)}
for i, k in enumerate("ABCDEF"):
    HEX[k] = 10 + i


def hex_to_dec(hex_s):
    L = len(hex_s)
    dec = 0
    for x in range(L):
        dec += HEX[hex_s[L - 1 - x]] * 16**x
    return dec


def dec_to_bin(dec):
    bin_s = ""
    while dec > 0:
        bin_s = str(dec % 2) + bin_s
        dec //= 2
    return "0" + bin_s


def hex_to_bin(hex_s):
    return dec_to_bin(hex_to_dec(hex_s))


for tc in range(1, T + 1):
    N, hex_s = input().split()
    print(f"#{tc} {hex_to_bin(hex_s)}")
