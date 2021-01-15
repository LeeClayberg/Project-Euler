import functools

factorials = dict()
for i in range(0, 10):
    count = 1
    for j in range(1, i+1):
        count *= j
    factorials[i] = count

past_numbers = dict()
total_count = 0
for a in range(1, 1000001):
    current_chain = set()
    current_num = a
    current_chain.add(current_num)
    check = True
    for _ in range(59):
        current_num = functools.reduce(lambda x, y: x + y, list(map(lambda a: factorials[int(a)], str(current_num))), 0)
        if current_num in current_chain:
            check = False
            break
        current_chain.add(current_num)
    current_num = functools.reduce(lambda x, y: x + y, list(map(lambda a: factorials[int(a)], str(current_num))), 0)
    if check and current_num in current_chain:
        total_count += 1
print(f"Total: {total_count}")

