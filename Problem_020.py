num = 100

product = 1
for i in range(1,num + 1):
    product *= i

digit_str_list = list(str(product))

sum = 0
for num in digit_str_list:
    sum += int(num)

print(sum)