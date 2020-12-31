
total = 0
for i in range(1, 1000):
    total += pow(i, i)
last_10 = ''.join(str(total)[-10:])
print(last_10)