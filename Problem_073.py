import math

count = 0
lower = 1.0 / 3.0
upper = 1.0 / 2.0
for d in range(2, 12001):
    for n in range(1, d):
        if lower < n / d < upper and math.gcd(d, n) == 1:
            count += 1
print(count)
