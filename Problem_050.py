from Extra_File import get_primes_up_to
import functools

def get_sum(l):
    return functools.reduce(lambda x, y: x+y, l, 0)


primes = get_primes_up_to(1000000)
primes_list = list(primes)
primes_list.sort()

longest_num = 0
longest_sum = 0

for num in reversed(primes_list):
    current_start = 0
    current_end = 1
    current_sum = 0
    while current_sum < num:
        current_sum = get_sum(primes_list[current_start: current_end + 1])
        current_end += 1
    while current_sum > num:
        current_sum = get_sum(primes_list[current_start + 1: current_end])
        current_start += 1
    if current_sum == num and current_end-current_start > longest_sum:
        longest_sum = current_end-current_start
        longest_num = num
print(longest_num)



