
max_count = 0
max_num = 0
for num in range(1, 1000000):
    count = 1

    curr_num = num
    while curr_num > 1:
        count += 1

        if curr_num % 2 == 0:
            curr_num /= 2
        else:
            curr_num = 3 * curr_num + 1

    if count > max_count:
        max_count = count
        max_num = num

    if num % 10000 == 0:
        print(num)

print(f"{max_num} with {max_count} steps")
