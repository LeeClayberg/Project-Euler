import math


def prime_check(num):
    for j in range(3, int(math.sqrt(num))+1):
        if num % j == 0:
            return False
    return True


total_count = 1
prime_count = 0
current = 1
for adder in range(1, 100000):
    for i in range(0, 4):
        total_count += 1
        current += (adder * 2)
        if prime_check(current):
            prime_count += 1
    if prime_count / total_count < 0.10:
        print(f"Len: {adder * 2 + 1}")
        break
