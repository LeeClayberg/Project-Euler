
check_points = set({1, 10, 100, 1000, 10000, 100000, 1000000})

decimal = ""
for a in range(1, 1000000):
    decimal += str(a)

total_product = 1
for index, digit in enumerate(decimal):
    if index+1 in check_points:
        total_product *= int(digit)
print(total_product)