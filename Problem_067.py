
pyramid = []
# Read in stuff
with open("./extra_files/p067_triangle.txt", "r") as file_stream:
    while True:
        line = file_stream.readline()
        if not line:
            break
        pyramid.append(list(map(lambda x: int(x), line[:-1].split(" "))))

working = list(reversed(pyramid))
for i in range(1, len(pyramid)):
    for j in range(0, len(working[i])):
        max_under = max(working[i-1][j], working[i-1][j+1])
        working[i][j] += max_under

print(working[len(pyramid)-1][0])
