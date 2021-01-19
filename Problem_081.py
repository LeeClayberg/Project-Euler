matrix = []
# Read in stuff
with open("./extra_files/p081_matrix.txt", "r") as file_stream:
    while True:
        line = file_stream.readline()
        if not line:
            break
        matrix.append(list(map(lambda x: int(x), line.split(","))))

current_lowest = [[0 for _ in range(len(matrix))] for _ in range(len(matrix))]


def update_value(point):
    top, left = 1000000, 1000000
    if point[1] > 0:
        top = current_lowest[point[0]][point[1] - 1]
    if point[0] > 0:
        left = current_lowest[point[0] - 1][point[1]]
    if point == (0, 0):
        top, left = 0, 0
    current_lowest[point[0]][point[1]] = matrix[point[0]][point[1]] + min(top, left)


for a in range(len(matrix)):
    for b in range(a+1):
        p = (b, a - b)
        update_value(p)

for a in reversed(range(len(matrix))):
    for b in range(a):
        p = (len(matrix)+b-a, len(matrix) - 1 - b)
        update_value(p)
print(current_lowest[len(matrix)-1][len(matrix)-1])
