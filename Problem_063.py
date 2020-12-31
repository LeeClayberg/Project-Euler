import math
count = 0
for i in range(1, 10):
    for j in range(1, math.floor(math.log(10)/(math.log(10)-math.log(i)))+1):
        if len(str(pow(i, j))) == j:
            count += 1
print(f"Count: {count}")
