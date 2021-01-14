from Extra_File import prime_factorization_of, get_primes_up_to
import functools

primes = get_primes_up_to(1000000)
current_num = 1
current_triangle = 1
biggest_so_far = 0

while True:
    # Get triangle number
    current_num += 1
    current_triangle += current_num

    # Factor count
    count = functools.reduce(lambda x, y: x * (y[1] + 1), prime_factorization_of(current_triangle, primes), 1)

    if count > biggest_so_far:
        biggest_so_far = count

    if count >= 500:
        break

# Print result
print(current_triangle)
