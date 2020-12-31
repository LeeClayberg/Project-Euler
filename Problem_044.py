import math


def find_first_lowest():
    lowest = 10000000000
    num_1 = 2
    while num_1 < 100000:
        for num_2 in range(1, num_1):
            p_1 = num_1 * (3 * num_1 - 1) / 2
            p_2 = num_2 * (3 * num_2 - 1) / 2
            sub = math.fabs(p_1 - p_2)
            add = p_1 + p_2
            if not ((1 + math.sqrt(1 + 24 * sub)) / 6).is_integer():
                continue
            if not ((1 + math.sqrt(1 + 24 * add)) / 6).is_integer():
                continue
            return int(sub)
        num_1 += 1
    return lowest


print(find_first_lowest())