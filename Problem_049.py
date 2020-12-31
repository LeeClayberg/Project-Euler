from Extra_File import get_primes_up_to
from itertools import permutations

primes = get_primes_up_to(10000)
primes_list = list(primes)
primes_list.sort()

used = set()
for num in primes_list:
    perms = permutations(list(str(num)), 4)
    perms = list(map(lambda x: int(''.join(x)), perms))
    perms = list(filter(lambda x: x >= 1000 and x in primes and x != num, perms))
    perms.sort()

    for a in perms:
        for b in filter(lambda x: x != a, perms):
            if a - num == b - a and not set({num, a, b}).issubset(used):
                used.add(num)
                used.add(a)
                used.add(b)
                print(f"{num}{a}{b}")
