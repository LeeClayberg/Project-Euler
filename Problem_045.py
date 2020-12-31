tri_numbers = set()
pent_numbers = set()
hex_numbers = set()

for n in range(2, 100000):
    tri_numbers.add(n * (n + 1) / 2)

for n in range(2, 100000):
    pent_numbers.add(n * (3 * n - 1) / 2)

for n in range(2, 100000):
    hex_num = n * (2 * n - 1)
    if hex_num in tri_numbers and hex_num in pent_numbers and hex_num != 40755:
        print(hex_num)
        break
