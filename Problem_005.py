
number = 1
while True:
    divisor = 2
    while divisor <= 20:
        if number % divisor != 0:
            break
        divisor += 1

    if divisor > 20:
        break
    else:
        number += 1
print(number)
