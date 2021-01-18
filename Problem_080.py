from decimal import *
import functools

getcontext().prec = 102

total = 0
for i in range(1, 101):
    num = Decimal(i).sqrt()
    if int(num) != num:
        str_n = str(num).replace(".", "")[:100]
        g = functools.reduce(lambda x, y: x+y, list(map(lambda a: int(a), str_n)), 0)
        total += g
print(total)
