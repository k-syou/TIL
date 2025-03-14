result = 0
for i in range(1 << 5):
    print(bin(i).replace('0b', '').zfill(5))
    cnt = 0
    for j in range(5):
        if (i >> j) & 0b1:
            cnt += 1
    if cnt >= 2:
        result += 1
print(result)