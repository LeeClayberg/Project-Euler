from Extra_File import get_primes_up_to

primes = sorted(list(get_primes_up_to(100)))
seen_before = dict()


def find_choices_rec(idx, num):
    if num == 0:
        return 1
    if num == 1:
        return 0
    if (idx, num) not in seen_before.keys():
        choices = 0
        i = 0
        while primes[i] < idx:
            for b in range(1, num // primes[i] + 1):
                extra = num - primes[i] * b
                choices += find_choices_rec(primes[i], extra)
            i += 1
        seen_before[(idx, num)] = choices
        return choices
    else:
        return seen_before[(idx, num)]


def find_choices(num):
    return find_choices_rec(num-1, num)


num = 4
while True:
    if find_choices(num) > 5000:
        print(num)
        break
    num += 1
