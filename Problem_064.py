import math


# Formula found on Wikipedia
def calc_period_len(n):
    root = int(math.sqrt(n))
    m = 0
    d = 1
    a = root
    period = 0
    while a != 2 * root:
        m = d * a - m
        d = int((n - m * m) / d)
        a = int((root + m) / d)
        period += 1
    return period


count = 0
for i in range(1, 10001):
    if math.sqrt(i) == int(math.sqrt(i)):
        continue
    if calc_period_len(i) % 2 != 0:
        count += 1
print(count)
