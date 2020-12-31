import math

prime_counter = 2
current_num = 5
while True:
    check = True
    for i in range(2, int(math.sqrt(current_num))+1):
        if current_num % i == 0:
            check = False
            break
    if check:
        prime_counter += 1
        if prime_counter == 10001:
            print(current_num)
            break
    current_num += 1
