from Extra_File import to_binary, get_primes_up_to

primes = get_primes_up_to(1000000)
prime_list = list(primes)
prime_list.sort()


def find_possible_replacements(number, family_len):
    for i in range(1, pow(2, len(str(number)))):
        binary = to_binary(i)
        count = 0
        vvv = []
        for repl in range(0, 10):
            if count + (10 - repl) < family_len:
                break
            form = list(map(lambda x: str(int(x) * repl) if int(x) != 0 else '-1', list(str(binary))))
            while len(form) < len(str(number)):
                form = ['-1'] + form
            str_num = list(str(number))
            new_num = []
            for j in range(0, len(str_num)):
                if int(form[j]) >= 0:
                    new_num += [form[j]]
                else:
                    new_num += [str_num[j]]
            new_num = int(''.join(list(new_num)))
            if new_num in primes and len(str(new_num)) == len(str(number)):
                count += 1
                vvv += [new_num]
        if count == family_len and count > 0:
            print(vvv[0])
            return True
    return False


def find_answer():
    for num in prime_list:
        check = find_possible_replacements(num, 8)
        if check:
            break


find_answer()
