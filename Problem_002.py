
num_1 = 1
num_2 = 2

total = 0
while num_2 < 4000000:
    if num_2 % 2 == 0:
        total += num_2
    num_3 = num_2
    num_2 = num_2 + num_1
    num_1 = num_3
print(total)
