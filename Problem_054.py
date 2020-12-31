import functools
from collections import Counter


rank = dict({'2': 0, '3': 1, '4': 2, '5': 3, '6': 4, '7': 5, '8': 6,
             '9': 7, 'T': 8, 'J': 9, 'Q': 10, 'K': 11, 'A': 12})


def get_data(hand):
    highest_card = functools.reduce(lambda x, y: max(x, rank[y[0]]), hand, 0)
    values = list(map(lambda x: rank[x[0]], hand))
    card_ranking = list(reversed(sorted(values)))
    straight = (sorted(values) == list(range(min(values), max(values) + 1)))
    flush = (1 == len(set(list(map(lambda x: x[1], hand)))))
    a_kind = Counter(x for x in values)
    which_kind = dict()
    for key, value in a_kind.items():
        if value not in which_kind.keys():
            which_kind[value] = []
        which_kind[value].append(key)
    return {'highest_card': highest_card, 'card_ranking': card_ranking, 'straight': straight, 'flush': flush, 'kinds': which_kind}


def check_straight_flush(info_1, info_2):
    num_1 = num_2 = 0
    if info_1['straight'] and info_1['flush']:
        num_1 = info_1['highest_card']
    if info_2['straight'] and info_2['flush']:
        num_2 = info_2['highest_card']
    return num_1 - num_2


def check_four_of_a_kind(info_1, info_2):
    num_1 = num_2 = 0
    if 4 in info_1['kinds']:
        num_1 = functools.reduce(lambda x, y: max(x, y), info_1['kinds'][4], 0)
    if 4 in info_2['kinds']:
        num_2 = functools.reduce(lambda x, y: max(x, y), info_2['kinds'][4], 0)
    return num_1 - num_2


def check_full_house(info_1, info_2):
    num_1 = num_2 = 0
    if 3 in info_1['kinds'] and 2 in info_1['kinds']:
        num_1 = info_1['kinds'][3][0]
    if 3 in info_2['kinds'] and 2 in info_2['kinds']:
        num_2 = info_2['kinds'][3][0]
    return num_1 - num_2


def check_flush(info_1, info_2):
    num_1 = num_2 = 0
    if info_1['flush']:
        num_1 = info_1['highest_card']
    if info_2['flush']:
        num_2 = info_2['highest_card']
    return num_1 - num_2


def check_straight(info_1, info_2):
    num_1 = num_2 = 0
    if info_1['straight']:
        num_1 = info_1['highest_card']
    if info_2['straight']:
        num_2 = info_2['highest_card']
    return num_1 - num_2


def check_three_of_a_kind(info_1, info_2):
    num_1 = num_2 = 0
    if 3 in info_1['kinds']:
        num_1 = info_1['kinds'][3][0]
    if 3 in info_2['kinds']:
        num_2 = info_2['kinds'][3][0]
    return num_1 - num_2


def check_two_pairs(info_1, info_2):
    num_1 = num_2 = 0
    if 2 in info_1['kinds'] and len(info_1['kinds'][2]) == 2:
        num_1 = functools.reduce(lambda x, y: max(x, y), info_1['kinds'][2], 0)
    if 2 in info_2['kinds'] and len(info_2['kinds'][2]) == 2:
        num_2 = functools.reduce(lambda x, y: max(x, y), info_2['kinds'][2], 0)
    return num_1 - num_2


def check_pair(info_1, info_2):
    num_1 = num_2 = 0
    if 2 in info_1['kinds']:
        num_1 = info_1['kinds'][2][0]
    if 2 in info_2['kinds']:
        num_2 = info_2['kinds'][2][0]
    return num_1 - num_2


player_1 = []
player_2 = []
# Read in stuff
with open("./extra_files/p054_poker.txt", "r") as file_stream:
    for i in range(0, 1000):
        cards = file_stream.readline().replace("\n", "").split(" ")
        tuples = list(map(lambda s: [s[0], s[1]], cards))
        player_1 += [tuples[0: 5]]
        player_2 += [tuples[5: 10]]

count = 0
for hand_1, hand_2 in zip(player_1, player_2):
    hand_1_info = get_data(hand_1)
    hand_2_info = get_data(hand_2)

    # Straight Flush check
    check_1 = check_straight_flush(hand_1_info, hand_2_info)
    if check_1 > 0:
        count += 1
        continue
    elif check_1 < 0:
        continue

    # Four of a Kind
    check_2 = check_four_of_a_kind(hand_1_info, hand_2_info)
    if check_2 > 0:
        count += 1
        continue
    elif check_2 < 0:
        continue

    # Full House
    check_3 = check_full_house(hand_1_info, hand_2_info)
    if check_3 > 0:
        count += 1
        continue
    elif check_3 < 0:
        continue

    # Flush
    check_4 = check_flush(hand_1_info, hand_2_info)
    if check_4 > 0:
        count += 1
        continue
    elif check_4 < 0:
        continue

    # Straight
    check_5 = check_straight(hand_1_info, hand_2_info)
    if check_5 > 0:
        count += 1
        continue
    elif check_5 < 0:
        continue

    # Three of a kind
    check_6 = check_three_of_a_kind(hand_1_info, hand_2_info)
    if check_6 > 0:
        count += 1
        continue
    elif check_6 < 0:
        continue

    # Two pairs
    check_7 = check_two_pairs(hand_1_info, hand_2_info)
    if check_7 > 0:
        count += 1
        continue
    elif check_7 < 0:
        continue

    # Pair
    check_8 = check_pair(hand_1_info, hand_2_info)
    if check_8 > 0:
        count += 1
        continue
    elif check_8 < 0:
        continue

    # Highest card
    i = 0
    while hand_1_info['card_ranking'][i] == hand_2_info['card_ranking'][i]:
        i += 1
    if hand_1_info['card_ranking'][i] > hand_2_info['card_ranking'][i]:
        count += 1

print(count)
