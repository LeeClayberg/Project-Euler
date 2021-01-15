
triples_found = set()
counts = dict()
limit = 1500
for m in range(2, limit):
    for n in range(1, m + 1):
        a = m * m - n * n
        b = 2 * m * n
        c = m * m + n * n
        if a == 0 or b == 0 or c == 0:
            break
        mult = 1
        while True:
            triple = (a*mult, b*mult, c*mult)
            count = sum(triple)
            if count > 1500000:
                break
            triple_str = ",".join(list(map(lambda x: str(x), sorted(triple))))
            if triple_str not in triples_found:
                triples_found.add(triple_str)
                if count not in counts:
                    counts[count] = 0
                counts[count] += 1
            mult += 1
total_numbers = 0
for key in counts.keys():
    if counts[key] == 1:
        total_numbers += 1
print(f"Total: {total_numbers}")
