import functools

store = dict()
answers = set()


def in_store(num1, num2):
    row_list = store.get(num1, 0)
    if row_list == 0:
        return False
    return num2 in row_list


def add_store(num1, num2):
    if num1 not in store.keys():
        store[num1] = set()
    store[num1].add(num2)
    if num2 not in store.keys():
        store[num2] = set()
    store[num2].add(num1)


def pandigital(str):
    return len(str) == 9 and len(set(list(str))) == 9 and '0' not in str


for i in range(100, 10000):
    for j in range(2, int(i/2)+1):
        if i % j == 0 and not in_store(j, i/j):
            if pandigital(f"{j}{int(i/j)}{i}"):
                print(f"{i}")
                answers.add(i)
                add_store(j, i/j)
print(functools.reduce(lambda x, y: x+y, answers))
