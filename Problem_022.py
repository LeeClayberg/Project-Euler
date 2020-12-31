import pandas
import functools

data = pandas.read_csv('./extra_files/p022_names.txt', sep=",", header=None, keep_default_na=False)
names = data.T
names.sort_values(by=0, inplace=True)
names = names.values.tolist()
names = functools.reduce(lambda x, y: x+y, names)


def caluclate_score(i, name):
    sum = 0
    for letter in name.lower():
        sum += (ord(letter) - 96)
    return sum * (i+1)


scores = list(map(lambda pair: caluclate_score(pair[0], pair[1]), enumerate(names)))
total = functools.reduce(lambda x, y: x+y, scores)
print(total)
