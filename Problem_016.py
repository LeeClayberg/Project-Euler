
num_str = str(pow(2, 1000))

digit_str_list = list(num_str)

sum = 0
for num in digit_str_list:
    sum += int(num)

print(sum)