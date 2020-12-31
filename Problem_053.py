import math

total_over = 0
for n in range(23, 101):
    r = 1
    n_fac = math.factorial(n)
    while r <= n:
        r_fac = math.factorial(r)
        rn_fac = math.factorial(n-r)
        if n_fac / (r_fac * rn_fac) > 1000000:
            total_over += 1
        r += 1
print(total_over)
