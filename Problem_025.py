number1 = 1
number2 = 1
switch = True

count = 2
while len(str(number1)) != 1000 and len(str(number2)) != 1000:
    if switch:
        number1 = number1 + number2
    else:
        number2 = number1 + number2
    switch = not switch
    count += 1

print(count)