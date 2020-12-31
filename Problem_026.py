from decimal import *

getcontext().prec = 2600

largest = 0
number = 0
for i in range(2, 1000):
    num = Decimal(1) / Decimal(i)
    num_str = str(num).split(".")[1][:-1]
    if len(num_str) > 6:
        for j in range(2, len(num_str)):
            repeater = num_str[-j:]
            repeater += repeater
            found = num_str.find(repeater)
            if found != -1:
                if largest < len(num_str[-j:]):
                    largest = len(num_str[-j:])
                    number = i
                break
print(f"Number: {number}\tCycle: {largest}")