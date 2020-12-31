
for i in range(1, 1000000):
    matcher = list(str(i))
    matcher.sort()
    check = True
    for m in range(2, 7):
        match = list(str(i * m))
        match.sort()
        if ''.join(matcher) != ''.join(match):
            check = False
            break
    if check:
        print(i)
        break
