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


# Get composite numbers up to a specified number
# Returns a set
def get_composites_up_to(num):
    composite_numbers = set()
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
        if not checker[i]:
            composite_numbers.add(i)

    return composite_numbers


# Converts number to binary representation
# Returns an integer
def to_binary(num):
    number = num
    power = pow(2, 19)
    bin = ""
    while power >= 1:
        if number >= power:
            bin += '1'
            number -= power
        else:
            bin += '0'
        power /= 2
    return int(bin)
