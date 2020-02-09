from collections import Counter

YACHT = 0
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11


def score(dice, category):
    if category in [1,2,3,4,5,6]:
        return sum([d for d in dice if d == category])
    elif category == FULL_HOUSE:
        print([i[1] for i in Counter(dice).most_common()])
        if sorted([i[1] for i in Counter(dice).most_common()]) == [2,3]: return sum(dice)
    elif category == FOUR_OF_A_KIND:
        i, j = Counter(dice).most_common()[0]
        if j >= 4: return i * 4
    elif category == LITTLE_STRAIGHT:
        if sorted(dice) == [1, 2, 3, 4, 5]: return 30
    elif category == BIG_STRAIGHT:
        if sorted(dice) == [2, 3, 4, 5, 6]: return 30
    elif category == YACHT:
        if len(set(dice)) == 1: return 50
    elif category == CHOICE: return sum(dice)
    return 0

print(score([3, 3, 3, 3, 3], FOUR_OF_A_KIND))