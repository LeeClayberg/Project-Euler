
seen_before = dict()


def find_choices_rec(idx, num):
    if num == 0:
        return 1
    if (idx, num) not in seen_before.keys():
        choices = 0
        for i in range(1, idx+1):
            for b in range(1, num // i + 1):
                extra = num - i * b
                choices += find_choices_rec(i-1, extra)
        seen_before[(idx, num)] = choices
        return choices
    else:
        return seen_before[(idx, num)]


def find_choices(num):
    return find_choices_rec(num-1, num)


print(find_choices(100))
