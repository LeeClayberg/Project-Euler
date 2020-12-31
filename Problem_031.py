
numbers = [1, 2, 5, 10, 20, 50, 100, 200]


def find_choices_rec(idx, num):
    if idx == 0:
        return 1
    choices = 1
    for i in range(1, idx+1):
        for b in range(1, int(num / numbers[i])+1):
            extra = num - b * numbers[i]
            choices += find_choices_rec(i-1, extra)
    return choices


def find_choices(num):
    return find_choices_rec(num, numbers[num])


print(find_choices(7))


