from fractions import Fraction


def formula(n):
    total = Fraction(0)
    for j in range(1, n):
        total = (Fraction(1) / (Fraction(2) + total))
    return total + Fraction(1)


count = 0
for i in range(2, 1000):
    dec = formula(i)
    if len(str(dec.numerator)) > len(str(dec.denominator)):
        count += 1
print(f"Count: {count}")
