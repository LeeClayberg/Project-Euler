import math
from fractions import Fraction
import functools


e = [2]
counter = 2
while len(e) < 100:
    e += [1, counter, 1]
    counter += 2
e = e[0:100]


f = 0
for h in reversed(e):
    if f == 0:
        f = Fraction(1, h)
    else:
        f = Fraction(h) + Fraction(f.denominator, f.numerator)

print(f"Sum: {functools.reduce(lambda x, y: int(x)+int(y), str(f.numerator), 0)}")
