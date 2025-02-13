# 5356. 의석이의 세로로 말해요

T = int(input())

for tc in range(1, T + 1):
    words = [input() for _ in range(5)]
    words_len = [len(s) for s in words]
    res = ""
    for i in range(max(words_len)):
        for j in range(5):
            if i < words_len[j]:
                res += words[j][i]
    print(f"#{tc} {res}")
