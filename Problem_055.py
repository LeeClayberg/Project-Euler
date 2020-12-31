
def flip_number(num):
    return int(''.join(list(reversed(list(str(num))))))


def is_palindrome(num):
    return num == flip_number(num)


count = 0
for num in range(1, 10000):
    current_num = num
    check = True
    for i in range(0, 50):
        current_num += flip_number(current_num)
        if is_palindrome(current_num):
            check = False
            break
    if check:
        count += 1
print(f"Count: {count}")
