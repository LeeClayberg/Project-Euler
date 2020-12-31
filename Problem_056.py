import functools

maximum = 0
for a in range(1, 100):
    for b in range(1, 100):
        digits = list(map(lambda x: int(x), list(str(pow(a, b)))))
        total = functools.reduce(lambda x, y: x+y, digits, 0)
        if total > maximum:
            maximum = total
print(maximum)