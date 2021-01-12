from itertools import permutations

inner_loop = list(permutations([1, 2, 3, 4, 5], 5))
outer_loop = list(permutations([6, 7, 8, 9, 10], 5))

max_16_digit_number = 0
for inner in inner_loop:
    for outer in outer_loop:
        full_format = [0 for _ in range(15)]
        for idx_1, a in enumerate(inner):
            full_format[2+3*idx_1] = a
            full_format[(4+3*idx_1) % 15] = a
        for idx_2, b in enumerate(outer):
            full_format[3*idx_2] = b
        counts = [full_format[c*3] + full_format[c*3+1] + full_format[c*3+2] for c in range(5)]
        if len(set(counts)) == 1:
            shifts_to_do = outer.index(min(outer))
            for _ in range(shifts_to_do * 3):
                full_format.append(full_format.pop(0))
            combined_num = int("".join(list(map(lambda x: str(x), full_format))))
            max_16_digit_number  = max(max_16_digit_number, combined_num)
print(max_16_digit_number)
