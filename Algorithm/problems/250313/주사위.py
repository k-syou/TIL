N = 3

dice = []


def roll_dice(roll, num):
    if roll == 3:
        print(dice)
        return
    for i in range(num, 7):
        dice.append(i)
        roll_dice(roll + 1, i)
        dice.pop()

roll_dice(0, 1)