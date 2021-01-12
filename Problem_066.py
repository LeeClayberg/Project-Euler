import math
from fractions import Fraction
from Extra_File import get_repeating
from decimal import *

getcontext().prec = 150

current_highest_x = 0
current_highest_D = 1
for d in range(1001):
    if int(math.sqrt(d)) != math.sqrt(d):
        current_number = Decimal(d).sqrt()
        floor = int(current_number)
        continued_fraction = [floor]
        for _ in range(150):
            current_number = Decimal(1.0) / (current_number - Decimal(floor))
            floor = int(current_number)
            continued_fraction.append(floor)
        repeater = get_repeating(continued_fraction[1:], True)
        size = len(repeater)
        if size % 2 == 0:
            digits = continued_fraction[:size]
        else:
            digits = continued_fraction[:2*size]
        total = Fraction(digits[-1])
        for a in list(reversed(digits))[1:]:
            total = Fraction(a) + (Fraction(1) / (total if total != 0 else 1))
        common_divisor = math.gcd(total.numerator, total.denominator)
        x = int(total.numerator) // int(common_divisor)
        y = int(total.denominator) // int(common_divisor)
        if x > current_highest_x:
            current_highest_x = x
            current_highest_D = d

print(f"D= {current_highest_D}\t\tx= {current_highest_x}")
