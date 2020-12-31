import math


# Get primes up to a specified number
def get_primes_up_to(num):
    prime_numbers = set()
    checker = []

    for i in range(0, num):
        checker.append(True)

    for i in range(2, int(math.sqrt(num))+1):
        if checker[i]:
            counter = 2
            while i * counter < num:
                checker[i * counter] = False
                counter += 1

    for i in range(2, num):
        if checker[i]:
            prime_numbers.add(i)

    return prime_numbers


primes = get_primes_up_to(1000000)
count = 0
for num in primes:
    check = True
    for i in range(1, len(str(num))):
        new_number = int(f"{str(num)[-(len(str(num)) - i):]}{str(num)[:i]}")
        if new_number not in primes:
            check = False
            break
    if check:
        count +=1
print(count)