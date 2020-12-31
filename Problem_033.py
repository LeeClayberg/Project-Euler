
def simplify(num, den):
    new_num = num
    new_den = den
    divisor = 2
    while divisor <= new_num:
        if new_num % divisor == 0 and new_den % divisor == 0:
            new_num /= divisor
            new_den /= divisor
            divisor = 2
        else:
            divisor += 1
    return [int(new_num), int(new_den)]


total_num = 1
total_den = 1
for i in range(11, 100):
    if i % 10 != 0:
        end_digit = int(list(str(i))[-1])
        numerator = int(list(str(i))[0])
        check_start = end_digit * 10
        for j in range(check_start+1, check_start+10):
            start_digit = int(list(str(j))[0])
            denometer = int(list(str(j))[-1])
            correct_frac = i / j
            new_frac = numerator / denometer
            if correct_frac < 1 and correct_frac == new_frac:
                total_num *= i
                total_den *= j
                print(f"{i}/{j}")

frac = simplify(total_num, total_den)
print(f"Total: {frac[0]}/{frac[1]}")