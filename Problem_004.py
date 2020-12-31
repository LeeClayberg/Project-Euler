
largest = 0
for num_1 in range(100, 999):
    for num_2 in range(100, 999):
        product = num_1 * num_2
        if str(product) == ''.join(reversed(str(product))):
            largest = max(largest, product)
print(largest)
