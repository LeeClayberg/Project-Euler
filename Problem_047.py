from Extra_File import get_primes_up_to

primes = get_primes_up_to(1000000)
primes_list = list(primes)
primes_list.sort()

count_in_row = 0
for num in range(2, 1000000):
    current = num
    distinct_factors = 0
    index = 0
    while current >= primes_list[index]:
        while current >= primes_list[index]:
            if current % primes_list[index] == 0:
                current /= primes_list[index]
                distinct_factors += 1
                index += 1
                break
            index += 1
    if distinct_factors == 4:
        count_in_row += 1
    else:
        count_in_row = 0
    if count_in_row == 4:
        print(num-3)
        break
