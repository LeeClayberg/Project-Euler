import math


# Get primes up to a specified number
# Returns a set
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

total_sum = 0
for i in primes:
    if i > 10:
        num = str(i)
        check = True
        for j in range(1, len(num)):
            left_to_right = int(num[j:len(num)])
            right_to_left = int(num[0:-j])
            if left_to_right not in primes or right_to_left not in primes:
                check = False
                break
        if check:
            total_sum += int(num)
print(total_sum)
