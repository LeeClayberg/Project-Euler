
total_sum = 1
counter = 1

num = 2
while num <= 1000:
    for i in range(0, 4):
        counter += num
        total_sum += counter
    num += 2
print(total_sum)
