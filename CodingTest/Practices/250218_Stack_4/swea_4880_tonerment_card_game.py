def card_game(i, j):
    global cards
    if i == j:  # 토너먼트에서 한사람 만 붙은 경우
        return i  # 낮은 번호로 선택
    if j - i == 1:  # 둘의 차이가 1인 경우
        res_i, res_j = i, j
    else:  # 아닌 경우
        res_i, res_j = card_game(i, (i + j) // 2), card_game((i + j) // 2 + 1, j)

    # 해당 사람이 가지고 있는 카드의 숫자를 가져옴
    card_i = cards[res_i]
    card_j = cards[res_j]

    if card_i == card_j:  # 비긴경우 낮은 번호
        return res_i

    # 가위바위보 승자 결정
    if card_i - 1 == (card_j) % 3:
        # (보 -> 주먹 / 주먹 -> 가위 / 가위 -> 보)
        return res_i
    else:
        return res_j


for tc in range(1, int(input()) + 1):
    N = int(input())
    cards = [*map(int, input().split())]
    print(f"#{tc} {card_game(0, N-1) + 1}")
