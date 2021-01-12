import math
import functools


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


# Finds the repeating portion of the string
# Returns a string
def get_repeating(digits, start):
    prev_repeater = digits
    curr_repeater = list()
    for end_index in range(1, int(len(digits)/2)+1):
        repeater1 = digits[:end_index]
        repeater2 = repeater1 + repeater1
        found = compare_lists(digits[:2*end_index], repeater2)
        if found and (len(set(repeater1)) == len(set(digits)) or start) and len(repeater1) > len(curr_repeater):
            curr_repeater = repeater1
    if len(curr_repeater) == 0:
        curr_repeater = digits
    if len(curr_repeater) < len(prev_repeater):
        return get_repeating(curr_repeater, False)
    else:
        return curr_repeater


# Check if two lists are the same
# Returns a boolean
def compare_lists(list_1, list_2):
    return functools.reduce(lambda x, y : x and y, map(lambda p, q: p == q, list_1, list_2), True)
