from Extra_File import get_primes_up_to

primes = list(get_primes_up_to(1000000))

number = 600851475143

while number not in primes:
    index = 0
    while True:
        if number % primes[index] == 0:
            number /= primes[index]
            break
        else:
            index += 1
print(int(number))
