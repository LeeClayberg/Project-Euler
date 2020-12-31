from itertools import permutations


def check_prime(num):
    for i in range(2, int(num/2)+1):
        if num % i == 0:
            return False
    return True


f = []
for i in reversed(range(3, 10)):
    num = list('123456789')
    g = list(permutations(num[:i], i))
    h = list(map(lambda x: int(''.join(x)), g))
    f += h
f.sort(reverse=True)

for e in f:
    if check_prime(e):
        print(e)
        break

