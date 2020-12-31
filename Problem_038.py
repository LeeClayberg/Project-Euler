
largest = 0

for n in range(2, 10):
    for i in range(1, 10000):
        concat = ""
        for j in range(1, n):
            concat += str(i * j)
            if int(concat) > 999999999:
                break
        if int(concat) > largest and len(concat) == 9 and len(set(list(concat))) == 9 and '0' not in concat:
            largest = int(concat)
            num = i
            n_num = n
print(largest)
