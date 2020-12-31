import functools

factorials = dict({0: 1, 1: 1, 2: 2, 3: 6, 4: 24, 5: 120, 6: 720, 7: 5040, 8: 40320, 9: 362880})

total = 0
for i in range(3, 10000000):
    digits = list(map(lambda x: factorials.get(int(x)), list(str(i))))
    factorial_sum = functools.reduce(lambda x, y: x+y, digits)
    if factorial_sum == i:
        total += i
print(total)