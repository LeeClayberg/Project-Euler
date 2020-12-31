from math import sqrt

for a in range(998):
    for b in range(a+1, 998):
        c = sqrt(pow(a, 2) + pow(b, 2))
        if int(c) == c and c > b and a + b + c == 1000:
            print(f"{int(a * b * c)}")
            exit(0)
