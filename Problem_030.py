import functools

answers = set()
power = 7
for i in range(3, pow(10, power)+1):
    digits = str(i)
    digits = list(map(lambda x: pow(int(x), 5), digits))
    digit_sum = functools.reduce(lambda x, y: x+y, digits)
    if digit_sum == i:
        answers.add(i)
    if i % pow(10, power-1) == 0:
        print(f"{int(i / pow(10, power) * 100)}% Complete")
print(functools.reduce(lambda x, y: x+y, answers))
