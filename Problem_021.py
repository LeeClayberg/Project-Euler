import math
import functools
store = dict()

amicable_sum = 0
for i in range(1, 10001):
    # Gets factors and add them up
    factors = []
    for j in range(1, int(math.sqrt(i)+1)):
        if i % j == 0:
            factors.append(j)
    factors2 = list(map(lambda x: i/x, factors))
    factors = list(dict.fromkeys(factors + factors2))
    factor_sum = functools.reduce(lambda x, y: x+y, factors) - i

    # Checks for matching value
    val = store.get(factor_sum, 0)
    if val != 0:
        print(str(val) + " " + str(i))
        if val == i:
            amicable_sum += (factor_sum + i)
    store[i] = factor_sum

print(amicable_sum)