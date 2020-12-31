from Extra_File import get_primes_up_to
import functools

primes = get_primes_up_to(100000000)
primes_list = list(primes)
primes_list.sort()
primes_list = primes_list[:1100]
print(primes_list.index(8389))

pairs = set()
fours = set()


def check_concat(q, r):
    return int(str(q) + str(r)) in primes and int(str(r) + str(q)) in primes


# Find pairs that work
for n in primes_list:
    for m in primes_list:
        if m != n:
            if check_concat(m, n):
                a = min(n, m)
                b = max(n, m)
                pairs.add((a, b))
print(pairs)

# Find groups of four
for e in pairs:
    for f in pairs:
        if e != f and check_concat(e[0], f[0]) and check_concat(e[0], f[1]) and check_concat(e[1], f[0]) and check_concat(e[1], f[1]):
            numbers = list(e) + list(f)
            numbers.sort()
            fours.add(tuple(numbers))
print(fours)


for group in fours:
    common_ones = set()
    for i, num in enumerate(group):
        num_ones = set()
        for pair in pairs:
            if num == pair[0] and pair[1] not in group:
                num_ones.add(pair[1])
            if num == pair[1] and pair[0] not in group:
                num_ones.add(pair[0])
        if i > 0:
            common_ones = set.intersection(common_ones, num_ones)
        else:
            common_ones = num_ones
    if len(common_ones) > 0:
        all_numbers = list(group) + list(common_ones)
        print(f"Sum: {functools.reduce(lambda x, y: x + y, all_numbers, 0)}")
        break

