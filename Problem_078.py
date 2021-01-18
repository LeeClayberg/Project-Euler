
seen_before = dict()


def find_choices_rec(num):
    if num == 0:
        return 1
    if num < 0:
        return 0
    choices = 0
    for k in range(1, num+1):
        p_1_inner = num - (k * (3 * k - 1)) // 2
        if p_1_inner in seen_before:
            p_1 = seen_before[p_1_inner]
        else:
            p_1 = find_choices_rec(p_1_inner)
        p_2_inner = num - (k * (3 * k + 1)) // 2
        if p_2_inner in seen_before:
            p_2 = seen_before[p_2_inner]
        else:
            p_2 = find_choices_rec(p_2_inner)
        choices += pow(-1, k+1) * (p_1 + p_2)
    seen_before[num] = choices
    return choices


def find_choices(num):
    return find_choices_rec(num)


n = 2
while True:
    p_n = find_choices(n)
    if p_n % 1000000 == 0:
        break
    n += 1
print(f"n= {n}")
