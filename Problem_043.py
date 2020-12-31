from itertools import permutations
from Extra_File import get_primes_up_to

numbers = list(permutations(list('0123456789'), 10))
numbers = list(map(lambda x: ''.join(x), numbers))
primes = list(get_primes_up_to(18))
primes.sort()

total = 0
for num in numbers:
    check = True
    for i in range(1, len(num)-2):
        if int(num[i:i+3]) % primes[i-1] != 0:
            check = False
            break
    if check:
        total += int(num)
print(total)
