import functools

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
permutation = []

# Millionth lexicographic permutation
search = 999999
right = 0
left = 3628800


def move_from_index(index):
    permutation.append(numbers.pop(index))


while len(numbers) > 0:
    space_between = (left - right) / len(numbers)
    for i in range(0, len(numbers)):
        if right + space_between * i <= search < right + space_between * (i+1):
            move_from_index(i)
            left = right + space_between * (i+1)
            right = right + space_between * i
            break

permutation_str = list(map(lambda x: str(x), permutation))
permutation_str = functools.reduce(lambda x, y: str(x)+str(y), permutation_str)
print(permutation_str)
