# T = int(input())
# for tc in range(1, T + 1):
#     n, k = map(int, input().split())
#     display = [[0] * n for _ in range(4)]
#     cnt = 0
#     for t in range(1, k + 1):
#         # t : 시간
#         for i in range(4):
#             for j in range(n):
#                 x = i + j + 1  # 기준값
#                 if x % t == 0:  # 배수인 경우
#                     # ^ = xor
#                     # 0 ^ 1 = 1 | 1 ^ 1 = 0
#                     display[i][j] ^= 1
#     for i in range(4):
#         cnt += sum(display[i])
#     print(f"#{tc} {cnt}")

# """
# 4
# 5 3
# 35 39
# 93 70
# 569 138
# """


a = bin(int("ABC", 16)).replace("0b", "")
print(a)