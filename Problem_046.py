from Extra_File import get_primes_up_to, get_composites_up_to
import math

primes = get_primes_up_to(10000)
composites = list(get_composites_up_to(10000))
composites.sort()
odd_composites = filter(lambda x: x % 2 != 0, composites)

for composite in odd_composites:
    check = False
    for sq in range(1, int(math.sqrt(composite))):
        if composite - 2 * pow(sq, 2) in primes:
            check = True
            break
    if not check:
        print(composite)
        break