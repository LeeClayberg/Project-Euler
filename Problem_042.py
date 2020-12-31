triangle_numbers = set()

for i in range(1, 50):
    triangle_numbers.add(0.5 * i * (i+1))

with open("./extra_files/p042_words.txt", "r") as file_stream:
    words = file_stream.readline().replace("\"", "").split(",")
    count = 0
    for word in words:
        total = 0
        for letter in word:
            total += ord(letter) - 64
        if total in triangle_numbers:
            count += 1
    print(count)
