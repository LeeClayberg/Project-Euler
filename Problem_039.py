import math

perimeters = dict()

for i in range(3, 1000):
    for j in range(3, 1000):
        third = math.sqrt(pow(i, 2) + pow(j, 2))
        perim = int(third + i + j)
        if third.is_integer() and perim <= 1000:
            if perim not in perimeters.keys():
                perimeters[perim] = 1
            else:
                perimeters[perim] += 1

max_perim = max(perimeters, key=perimeters.get)
print(max_perim)

