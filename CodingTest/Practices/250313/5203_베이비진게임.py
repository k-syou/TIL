T = int(input())

def is_baby(card):
    sort_card = sorted(card)
    for i in range(2, len(card)):
        if sort_card[i-2] == sort_card[i-1] == sort_card[i]:
            return True
    set_card = sorted(set(card))
    if len(set_card) >= 3:
        for i in range(2, len(set_card)):
            if sort_card[i-2] + 2 == sort_card[i-1] + 1 == sort_card[i]:
                return True
    return False

def game(c1, c2):
    for i in range(2, 6):
        if is_baby(c1[:i+1]):
            return 1
        if is_baby(c2[:i+1]):
            return 2
    return 0

for tc in range(1, T + 1):
    card = [*map(int, input().split())]
    c1 = card[::2]
    c2 = card[1::2]
    print(f"#{tc} {game(c1, c2)}")
