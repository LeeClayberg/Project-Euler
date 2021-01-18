attempts = []
# Read in stuff
with open("./extra_files/p079_keylog.txt", "r") as file_stream:
    while True:
        line = file_stream.readline()
        if not line:
            break
        attempts.append(line[:-1])
# remove duplicates
attempts = list(set(attempts))

remember = dict()
for attempt in attempts:
    for i in range(0, len(attempt)):
        num = attempt[i]
        before = attempt[:i]
        if num not in remember:
            remember[num] = {'before': set()}
        remember[num]['before'] = remember[num]['before'].union(set(before))

answer = ""
while len(remember.keys()) > 0:
    current_pick = ""
    for key in remember.keys():
        if len(remember[key]['before']) == 0:
            current_pick = key
            break
    remember.pop(current_pick, None)
    for key in remember.keys():
        remember[key]['before'].discard(current_pick)
    answer += current_pick
print(answer)
