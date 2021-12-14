matrix = []
# Read in stuff
with open("./extra_files/p081_matrix.txt", "r") as file_stream:
    while True:
        line = file_stream.readline()
        if not line:
            break
        matrix.append(list(map(lambda x: int(x), line.split(","))))

# tuples are (y value, x value, count-up-to)
queue = list()
queue.append((0, 0, 0))

matrix_values = [[1000000 for x in range(80)] for y in range(80)]
while len(queue) > 0:
    y, x, count = queue.pop(0)
    if count + matrix[y][x] < matrix_values[y][x]:
        matrix_values[y][x] = count + matrix[y][x]
        if y > 0:
            queue.insert(0, (y - 1, x, matrix_values[y][x]))
        if y < 79:
            queue.insert(0, (y + 1, x, matrix_values[y][x]))
        if x > 0:
            queue.insert(0, (y, x - 1, matrix_values[y][x]))
        if x < 79:
            queue.insert(0, (y, x + 1, matrix_values[y][x]))

print(matrix_values[79][79])
