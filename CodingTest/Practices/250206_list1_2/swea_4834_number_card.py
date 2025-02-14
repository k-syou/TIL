# reverse 쓰지 말기

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    cards = [*map(int, input())]
    counts = [0] * 10
    for card in cards:
        counts[card] += 1

    max_count = 0
    max_value = 0

    for i in range(9, -1, -1):
        if counts[i] > max_count:
            max_count = counts[i]
            max_value = i

    print(f'#{tc} {max_value} {max_count}')