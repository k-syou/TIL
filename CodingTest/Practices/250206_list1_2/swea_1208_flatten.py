MAX = 101

for tc in range(1, 11):
    dump = int(input())
    num_dict = {i: 0 for i in range(MAX)}
    min_v = MAX
    max_v = 0
    for num in map(int, input().split()):
        num_dict[num] += 1
        if min_v > num:
            min_v = num
        if max_v < num:
            max_v = num

    for _ in range(dump):
        num_dict[max_v] -= 1
        num_dict[max_v - 1] += 1
        num_dict[min_v] -= 1
        num_dict[min_v + 1] += 1

        if num_dict[max_v] == 0:
            max_v -= 1

        if num_dict[min_v] == 0:
            min_v += 1

    print(f'#{tc} {max_v - min_v}')