
nums = set()
for a in range(2, 101):
    for b in range(2, 101):
        nums.add(pow(a, b))
print(len(nums))