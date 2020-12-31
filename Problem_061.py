import functools


def four_digit_numbers(func):
    numbers = []
    n = 1
    while True:
        number = func(n)
        if len(str(number)) == 4:
            numbers.append(number)
        if len(str(number)) == 5:
            break
        n += 1
    return numbers


def triangle(n):
    return int(n * (n + 1) / 2)


def square(n):
    return pow(n, 2)


def pentagonal(n):
    return int(n * (3 * n - 1) / 2)


def hexagonal(n):
    return n * (2 * n - 1)


def heptagonal(n):
    return int(n * (5 * n - 3) / 2)


def octagonal(n):
    return n * (3 * n - 2)


tri = four_digit_numbers(triangle)
sqr = four_digit_numbers(square)
pent = four_digit_numbers(pentagonal)
hex = four_digit_numbers(hexagonal)
hept = four_digit_numbers(heptagonal)
oct = four_digit_numbers(octagonal)

all = [tri, sqr, pent, hex, hept, oct]

after = dict()
for i, li in enumerate(all):
    for n1 in li:
        after[n1] = dict({"type": i, "connect": []})
        for n2 in [item for sublist in all[:i] + all[i+1:] for item in sublist]:
            if str(n2)[0:2] == str(n1)[-2:]:
                after[n1]['connect'].append(n2)


def find_answer(used, current, num):
    if len(used) == 6 and str(current[0])[0:2] == str(current[-1])[-2:]:
        print(f"{current}\tSum: {functools.reduce(lambda x, y: x + y, current, 0)}")
        return True

    if after[num]['type'] in used:
        return False
    for nxt in after[num]['connect']:
        check = find_answer(used + [after[num]['type']], current + [num], nxt)
        if check:
            return True
    return False


for key in after.keys():
    chk = find_answer([], [], key)
    if chk:
        break
