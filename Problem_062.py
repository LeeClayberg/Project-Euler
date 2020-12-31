
cubes = set()
for i in range(1, 10000):
    cubes.add(pow(i, 3))
cube_list = list(cubes)
cube_list.sort()

j = 0
while j < len(cube_list):
    num = cube_list[j]
    perms = [num]
    sort_num = sorted(list(str(num)))
    for k in cube_list[j+1:]:
        if len(str(k)) > len(str(num)):
            break
        if sorted(list(str(k))) == sort_num and len(str(k)) == len(str(num)):
            perms.append(k)
    if len(perms) == 5:
        print(f"Cube: {num}\t\t{perms}")
        break
    j += 1
