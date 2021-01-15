
total = 0
for n in range(2, 1000001):
    a = n
    result = n
    p = 2
    while pow(p, 2) <= n:
        if n % p == 0:
            while n % p == 0:
                n = n // p
            result = result * (1.0 - (1.0 / float(p)))
        p += 1
    if n > 1:
        result = result * (1.0 - (1.0 / float(n)))
    total += int(result)
print(total)
