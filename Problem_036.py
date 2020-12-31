
def to_binary(num):
    number = num
    power = pow(2, 19)
    bin = ""
    while power >= 1:
        if number >= power:
            bin += '1'
            number -= power
        else:
            bin += '0'
        power /= 2
    return int(bin)


def reverse_num(num):
    return int(''.join(list(reversed(str(num)))))


total = 0
for i in range(1, 1000000):
    binary = to_binary(i)
    if i == reverse_num(i) and binary == reverse_num(binary):
        total += i
print(total)
