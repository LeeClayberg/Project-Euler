import functools


# Read in stuff
with open("./extra_files/p059_cipher.txt", "r") as file_stream:
    codes = list(map(lambda x: int(x), file_stream.readline().split(",")))
part_codes = codes[0:10]
print(part_codes)

valid = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ?!',.()-/ :;$"
symbols = " ,'"

count = 0
for a in range(ord('a'), ord('z')+1):
    for b in range(ord('a'), ord('z') + 1):
        for c in range(ord('a'), ord('z') + 1):
            bbb = chr(a) + chr(b) + chr(c)
            message = ""
            for index, asc in enumerate(part_codes):
                ch = chr(asc ^ ord(bbb[index % 3]))
                if ch not in valid:
                    break
                message += ch
            if len(message) == len(part_codes) and message[2] in symbols:
                print(f"{message}\t\t{bbb}")


key = 'exp'
message = ""
for index, asc in enumerate(codes):
    message += chr(asc ^ ord(key[index % 3]))
print(message)

print(f"Sum: {functools.reduce(lambda x, y: x + ord(y), message, 0)}")










