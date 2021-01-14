
denom = 1000000
while denom % 7 != 0:
    denom -= 1
numer = denom // 7 * 3
print(numer - 1)
