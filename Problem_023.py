import functools
import math

abundant_numbers = set()
# Step 1 find abundant numbers
for i in range(1, 28123):
    # Gets factors and add them up
    factors = []
    for j in range(1, int(math.sqrt(i)+1)):
        if i % j == 0:
            factors.append(j)
    factors2 = list(map(lambda x: i/x, factors))
    factors = list(dict.fromkeys(factors + factors2))
    factor_sum = functools.reduce(lambda x, y: x+y, factors) - i

    if(factor_sum > i):
        abundant_numbers.add(i)

# Step 2 add up all numbers
total_sum = 0
for i in range(1, 28123):
    check = True
    for j in abundant_numbers:
        if i - j in abundant_numbers:
            check = False
            break
    if check:
        total_sum += i

print(abundant_numbers)
print(total_sum)